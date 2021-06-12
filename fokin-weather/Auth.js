import axios from "axios";
import * as SecureStore from "expo-secure-store";
import jwt_decode from "jwt-decode";

async function getValueStore(key) {
  return await SecureStore.getItemAsync(key);
}

async function setValueStore(key, value) {
  await SecureStore.setItemAsync(key, value);
}

export const Auth = {
  signIn: async (email, password) => {
    const { data } = await axios
      .post("http://10.0.2.2/api/users/login/", {
        email,
        password,
      })
      .catch(function (error) {
        if (error.response) {
          // The request was made and the server responded with a status code
          // that falls out of the range of 2xx
          if (
            error.response.status == 401 &&
            error.response.data.code &&
            error.response.data.code === "not_valid_login"
          ) {
            throw { loginFail: "아이디와 패스워드를 확인하세요." };
          } else {
            console.log("Error", error.response.status, error.response.data);
            throw {
              loginFail:
                "서버에서 예상하지 못한 에러 발생하였습니다. 잠시후 재시도 해주세요.",
            };
          }
        } else if (error.request) {
          // The request was made but no response was received
          // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
          // http.ClientRequest in node.js
          console.log("Error", error.request);
          throw {
            loginFail: "서버에 문제가 있습니다. 잠시후 재시도 해주세요.",
          };
        } else {
          // Something happened in setting up the request that triggered an Error
          console.log("Error", error.message);
          throw {
            loginFail: "알수 없는 에러가 발생하였습니다.",
          };
        }
      });
    // console.log("data", data);

    await setValueStore("refreshToken", data.refresh_token);
    console.log("refreshToken save complete", data.refresh_token);
    return data;
  },
  signUp: async (email, password1, password2) => {
    const {
      data: { access_token, refresh_token, user },
    } = await axios
      .post("http://10.0.2.2/api/users/signup/", {
        email,
        password1,
        password2,
      })
      .catch((err) => {
        console.log("Auth Error", err);
      });

    await setValueStore("refreshToken", refresh_token);
    return data;
  },
  signOut: () => {
    SecureStore.deleteItemAsync("refreshToken");
  },
  getTokenByRefreshToken: async (refreshToken) => {
    const {
      data: { access },
    } = await axios
      .post("http://10.0.2.2/api/users/token/refresh/", {
        refresh: refreshToken,
      })
      // .then((t) => console.log(t))
      .catch(function (error) {
        console.log("Auth access Error", error);
        if (error.response) {
          // The request was made and the server responded with a status code
          // that falls out of the range of 2xx
          if (
            error.response.status == 401 &&
            error.response.data.code &&
            error.response.data.code === "token_not_valid"
          ) {
            throw {
              loginExpired: "로그인 기간 만료되었습니다. 다시 로그인해주세요.",
            };
          } else {
            console.log(
              "Auth Error",
              error.response.status,
              error.response.data
            );
            throw {
              loginExpired: "로그인 기간 만료. 다시 로그인해주세요.",
            };
          }
        } else if (error.request) {
          // The request was made but no response was received
          // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
          // http.ClientRequest in node.js
          console.log("Auth Error", error.request);
          throw {
            loginExpired: "로그인 기간 만료. 다시 로그인해주세요.",
          };
        } else {
          // Something happened in setting up the request that triggered an Error
          console.log("Auth Error", error.message);
          throw {
            loginExpired: "로그인 기간 만료. 다시 로그인해주세요.",
          };
        }
      });

    console.log("Auth access", access);
    return access;
  },
  getRefreshTokenAtStorage: async () => {
    let refreshToken;

    try {
      refreshToken = await getValueStore("refreshToken");
    } catch (e) {
      console.log(e);
    }

    // token 없을경우
    if (!refreshToken) {
      console.log("Auth refreshToken Null");
      return null;
    }

    // After restoring token, we may need to validate it
    const { exp } = jwt_decode(refreshToken);
    if (Date.now() >= exp * 1000) {
      console.log("Auth refreshToken expired", Date.now(), exp * 1000);
      return null;
    }
    return refreshToken;
  },
  getAuthorizationHeader: (token) => `Bearer ${token}`,
};
