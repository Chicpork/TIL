import React from "react";
import { TouchableWithoutFeedback, TouchableOpacity } from "react-native";
import { List } from "react-native-paper";

export default function ListItem({ item, parentId }) {
  return (
    <List.Item
      title={item.title}
      description={item.description}
      left={(props) =>
        item.leftIcon && (
          <List.Icon
            {...props}
            icon={item.leftIcon.icon || null}
            color={item.leftIcon.color || null}
          />
        )
      }
      right={(props) =>
        item.rightIcon && (
          <TouchableOpacity
            onPress={(e) => {
              item.rightIcon.onPress &&
                item.rightIcon.onPress(parentId, item.id);
            }}
          >
            <List.Icon
              {...props}
              icon={
                item.rightIcon.isPressed
                  ? item.rightIcon.pressedIcon
                  : item.rightIcon.unPressedicon
              }
              color={
                item.rightIcon.icon == undefined ? null : item.rightIcon.color
              }
            />
          </TouchableOpacity>
        )
      }
      style={{
        width: "90%",
        alignSelf: "flex-end",
      }}
    />
  );
}
