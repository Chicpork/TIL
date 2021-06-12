import React from "react";
import { createMaterialBottomTabNavigator } from "@react-navigation/material-bottom-tabs";
import { createStackNavigator } from "@react-navigation/stack";
import HomeScreen from "./HomeScreen";
import LoginScreen from "./LoginScreen";
import ProfileScreen from "./ProfileScreen";
import HotFeedScreen from "./HotFeedScreen";
import DisclosureScreen from "./DisclosureScreen";
import SearchScreen from "./SearchScreen";
import UserScreen from "./UserScreen";
import CustomAppBar from "../components/CustomAppBar";

const Tab = createMaterialBottomTabNavigator();
const Stack = createStackNavigator();

const profileScreenOptions = {
  title: "Profile.",
};
const loginScreenOptions = {
  title: "Login.",
};

function HomeStackScreen() {
  return (
    <Stack.Navigator
      screenOptions={{
        header: (props) => <CustomAppBar {...props} />,
      }}
    >
      <Stack.Screen
        name="Home"
        component={HomeScreen}
        options={{
          title: "Home~~",
          subTitle: "HomeSub~",
        }}
        isLogin={true}
      />
      <Stack.Screen
        name="Profile"
        component={ProfileScreen}
        options={profileScreenOptions}
      />
      <Stack.Screen
        name="Login"
        component={LoginScreen}
        options={loginScreenOptions}
      />
      <Stack.Screen name="User" component={UserScreen} />
    </Stack.Navigator>
  );
}

function DisclosureStackScreen() {
  return (
    <Stack.Navigator
      screenOptions={{
        header: (props) => <CustomAppBar {...props} />,
      }}
    >
      <Stack.Screen name="Disclosure" component={DisclosureScreen} />
      <Stack.Screen
        name="Profile"
        component={ProfileScreen}
        options={profileScreenOptions}
      />
      <Stack.Screen
        name="Login"
        component={LoginScreen}
        options={loginScreenOptions}
      />
    </Stack.Navigator>
  );
}

function HotFeedStackScreen() {
  return (
    <Stack.Navigator
      screenOptions={{
        header: (props) => <CustomAppBar {...props} />,
      }}
    >
      <Stack.Screen name="HotFeed" component={HotFeedScreen} />
      <Stack.Screen
        name="Profile"
        component={ProfileScreen}
        options={profileScreenOptions}
      />
      <Stack.Screen
        name="Login"
        component={LoginScreen}
        options={loginScreenOptions}
      />
    </Stack.Navigator>
  );
}

function SearchStackScreen() {
  return (
    <Stack.Navigator
      screenOptions={{
        header: (props) => <CustomAppBar {...props} />,
      }}
    >
      <Stack.Screen name="Search" component={SearchScreen} />
      <Stack.Screen
        name="Profile"
        component={ProfileScreen}
        options={profileScreenOptions}
      />
      <Stack.Screen
        name="Login"
        component={LoginScreen}
        options={loginScreenOptions}
      />
    </Stack.Navigator>
  );
}

export default function screens() {
  return (
    <Tab.Navigator labeled={true}>
      <Tab.Screen
        name="Home"
        component={HomeStackScreen}
        options={{ tabBarIcon: "home" }}
      />
      <Tab.Screen
        name="Disclosure"
        component={DisclosureStackScreen}
        options={{ tabBarIcon: "file-document-outline" }}
      />
      <Tab.Screen
        name="HotFeed"
        component={HotFeedStackScreen}
        options={{ tabBarIcon: "fire" }}
      />
      <Tab.Screen
        name="Search"
        component={SearchStackScreen}
        options={{ tabBarIcon: "magnify" }}
      />
    </Tab.Navigator>
  );
}
