import React from "react";
import { Switch } from "react-native-paper";
import { PreferencesContext } from "../contexts/PreferencesContext";

export default function CustomSwitch() {
  const { toggleTheme, isThemeDark } = React.useContext(PreferencesContext);

  return <Switch value={isThemeDark} onValueChange={toggleTheme} />;
}
