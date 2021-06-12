import React from "react";

export const CustomContext = React.createContext({
  state: {},
  stateAction: {
    signIn: async () => {},
    signOut: () => {},
    signUp: async () => {},
    testSignIn: () => {},
    cAxios: () => {},
  },
});
