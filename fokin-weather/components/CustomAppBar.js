import React from "react";
import { StyleSheet } from "react-native";
import { Appbar } from "react-native-paper";
import { CustomSwitch } from "./CustomSwitch";
import { PreferencesContext } from "../contexts/PreferencesContext";

export default function CustomAppBar({ scene, navigation, previous, newNoti }) {
  const { options } = scene.descriptor;
  const title =
    options.headerTitle !== undefined
      ? options.headerTitle
      : options.title !== undefined
      ? options.title
      : scene.route.name;
  const { toggleTheme, isThemeDark } = React.useContext(PreferencesContext);

  return (
    <Appbar.Header>
      {previous ? <Appbar.BackAction onPress={navigation.goBack} /> : null}
      <Appbar.Content
        title={title}
        subtitle={options.subTitle !== undefined ? options.subTitle : null}
      />
      {!previous ? (
        <Appbar.Action
          icon={isThemeDark ? "moon-waning-crescent" : "white-balance-sunny"}
          onPress={() => toggleTheme()}
        />
      ) : null}
      {!previous ? (
        <Appbar.Action
          icon={newNoti ? "bell" : "bell-ring"}
          onPress={() => {}}
        />
      ) : null}
      {!previous ? (
        <Appbar.Action
          icon="account-circle"
          onPress={() => {
            navigation.navigate("Profile");
          }}
        />
      ) : null}
    </Appbar.Header>
  );
}
