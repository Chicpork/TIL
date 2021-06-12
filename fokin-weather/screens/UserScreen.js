import React from "react";
import { Text } from "react-native";
import { CustomContext } from "../contexts/CustomContext";
import customAxios from "../CustomAxios";

export default function UserScreen({ navigation }) {
  const {
    state: { isLogin },
    stateAction: { signOut },
  } = React.useContext(CustomContext);

  const t = async () => {
    const { data } = await customAxios.get("/users/user/");
    console.log("UserScreen", data);
  };

  React.useEffect(() => {
    t();
  }, []);

  return <Text>hi</Text>;
}
