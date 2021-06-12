import React from "react";
import { TouchableOpacity } from "react-native";
import { List, Divider } from "react-native-paper";
import { CustomContext } from "../contexts/CustomContext";

export default function ProfileScreen({ navigation }) {
  const {
    state: { isLogin, user },
    stateAction: { signOut },
  } = React.useContext(CustomContext);

  return (
    <List.Section>
      <TouchableOpacity
        onPress={(e) => {
          isLogin
            ? navigation.navigate("User")
            : navigation.navigate("Login");
        }}
      >
        <List.Item title={isLogin ? user.email : "로그인"} />
      </TouchableOpacity>
      <Divider />
      <TouchableOpacity
        onPress={(e) => {
          console.log("앱 설정이동");
        }}
      >
        <List.Item title="설정" />
      </TouchableOpacity>
      {isLogin ? (
        <TouchableOpacity
          onPress={(e) => {
            console.log("로그아웃");
            signOut();
            navigation.popToTop();
          }}
        >
          <List.Item title="로그아웃" />
        </TouchableOpacity>
      ) : null}
    </List.Section>
  );
}
