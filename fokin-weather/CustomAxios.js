import axios from "axios";
import { Auth } from "./Auth";

let isTokenRefreshing = false;
let refreshSubscribers = [];

const onTokenRefreshed = (accessToken) => {
  refreshSubscribers.map((callback) => callback(accessToken));
};

const addRefreshSubscriber = (callback) => {
  refreshSubscribers.push(callback);
};

const customAxios = axios.create({
  baseURL: "http://10.0.2.2/api",
  timeout: 1000,
});

customAxios.interceptors.request.use(
  function (config) {
    config.headers["Content-Type"] = "application/json; charset=utf-8";
    return config;
  },
  function (error) {
    console.log("customAxios Error", error);
    return Promise.reject(error);
  }
);
export default customAxios;

export const customAxiosAction = {
  setResponseInterceptors: (errorActionCB) => {
    if (!errorActionCB) {
      throw "errorActionCB is mandatory";
    }

    const setNewToken = async () => {
      try {
        const refreshToken = await Auth.getRefreshTokenAtStorage();
        const accessToken = await Auth.getTokenByRefreshToken(
          refreshToken
        ).catch((error) => {
          console.log("customAxios Error At getTokenByRefreshToken", error);
        });
        customAxios.defaults.headers.common["Authorization"] =
          Auth.getAuthorizationHeader(accessToken);
        // 새로운 토큰으로 지연되었던 요청 진행
        isTokenRefreshing = false;
        onTokenRefreshed(accessToken);
      } catch (error) {
        console.log("customAxios Error At setNewToken", error);
        onTokenRefreshed();
        errorActionCB();
      }
    };

    customAxios.interceptors.response.use(
      function (response) {
        // Any status code that lie within the range of 2xx cause this function to trigger
        // Do something with response data
        return response;
      },
      function (error) {
        // Any status codes that falls outside the range of 2xx cause this function to trigger
        // Do something with response error
        const {
          config,
          response: { data, status },
        } = error;
        const originalRequest = config;
        console.log("customAxios Error", error);

        if (status === 401) {
          if (
            !isTokenRefreshing &&
            data.code &&
            data.code === "token_not_valid"
          ) {
            // isTokenRefreshing이 false인 경우에만 token refresh 요청
            isTokenRefreshing = true;

            setNewToken();
          }

          // token이 재발급 되는 동안의 요청은 refreshSubscribers에 저장
          const retryOriginalRequest = new Promise((resolve) => {
            addRefreshSubscriber((accessToken) => {
              if (accessToken) {
                originalRequest.headers.Authorization =
                  Auth.getAuthorizationHeader(accessToken);
                resolve(customAxios(originalRequest));
              } else {
                Promise.reject(error);
              }
            });
          });
          return retryOriginalRequest;
        }
        return Promise.reject(error);
      }
    );
  },
};
