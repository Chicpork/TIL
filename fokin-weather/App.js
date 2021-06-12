import React from "react";
import {
  NavigationContainer,
  DefaultTheme as NavigationDefaultTheme,
  DarkTheme as NavigationDarkTheme,
} from "@react-navigation/native";
import {
  DarkTheme as PaperDarkTheme,
  DefaultTheme as PaperDefaultTheme,
  Provider as PaperProvider,
} from "react-native-paper";
import merge from "deepmerge";
import { PreferencesContext } from "./contexts/PreferencesContext";
import { CustomContext } from "./contexts/CustomContext";
import { Auth } from "./Auth";
import customAxios, { customAxiosAction } from "./CustomAxios";
import Loading from "./screens/Loading";
import HomeScreen from "./screens";

const CombinedDefaultTheme = merge(PaperDefaultTheme, NavigationDefaultTheme);
const CombinedDarkTheme = merge(PaperDarkTheme, NavigationDarkTheme);

export default function App() {
  const [isThemeDark, setIsThemeDark] = React.useState(false);

  let theme = isThemeDark ? CombinedDarkTheme : CombinedDefaultTheme;

  const toggleTheme = React.useCallback(() => {
    return setIsThemeDark(!isThemeDark);
  }, [isThemeDark]);

  const preferences = React.useMemo(
    () => ({
      toggleTheme,
      isThemeDark,
    }),
    [toggleTheme, isThemeDark]
  );

  const [state, dispatch] = React.useReducer(
    (prevState, action) => {
      switch (action.type) {
        case "RESTORE_TOKEN":
          return {
            ...prevState,
            token: action.token,
            isLoading: false,
            isLogin: action.token != null,
            user: action.user,
          };
        case "SIGN_IN":
          return {
            ...prevState,
            token: action.token,
            isLogin: action.token != null,
            user: action.user,
          };
        case "SIGN_OUT":
          return {
            ...prevState,
            token: null,
            isLogin: false,
            user: null,
          };
      }
    },
    {
      isLoading: true,
      token: null,
      isLogin: false,
      isTest: false,
      user: null,
    }
  );

  const stateAction = React.useMemo(
    () => ({
      signIn: async (email, password) => {
        const { access_token, user } = await Auth.signIn(email, password);

        customAxios.defaults.headers.common["Authorization"] =
          Auth.getAuthorizationHeader(access_token);
        dispatch({ type: "SIGN_IN", token: access_token, user });
      },
      signOut: () => {
        Auth.signOut();
        customAxios.defaults.headers.common["Authorization"] = null;
        dispatch({ type: "SIGN_OUT" });
      },
      signUp: async ({ email, password1, password2 }) => {
        const { access_token, user } = Auth.signUp(email, password1, password2);

        dispatch({ type: "SIGN_IN", token: access_token, user });
      },
      testSignIn: (access_token) => {
        dispatch({ type: "SIGN_IN", token: access_token });
      },
    }),
    []
  );

  const startUpLogin = async () => {
    try {
      const refreshToken = await Auth.getRefreshTokenAtStorage();
      console.log("App refreshToken", refreshToken);
      if (!refreshToken) {
        console.log("App not exists refresh token");
        return dispatch({ type: "RESTORE_TOKEN", token: null, user: null });
      }
      const accessToken = await Auth.getTokenByRefreshToken(refreshToken);
      console.log("App accessToken", accessToken);
      customAxios.defaults.headers.common["Authorization"] =
        Auth.getAuthorizationHeader(accessToken);
      const { data } = await customAxios.get("/users/user/");
      console.log("App data", data);
      dispatch({ type: "RESTORE_TOKEN", token: accessToken, user: data });
    } catch (error) {
      console.log("App startUpLogin", error);
      dispatch({ type: "RESTORE_TOKEN", token: null, user: null });
    }
  };

  React.useEffect(() => {
    console.log("App start");

    customAxiosAction.setResponseInterceptors(() => {
      dispatch({ type: "SIGN_OUT", token: null });
    });

    startUpLogin();
  }, []);

  return (
    <PreferencesContext.Provider value={preferences}>
      <CustomContext.Provider value={{ state, stateAction }}>
        <PaperProvider theme={theme}>
          {state.isLoading ? (
            <Loading />
          ) : (
            <NavigationContainer theme={theme}>
              <HomeScreen />
            </NavigationContainer>
          )}
        </PaperProvider>
      </CustomContext.Provider>
    </PreferencesContext.Provider>
  );
}
