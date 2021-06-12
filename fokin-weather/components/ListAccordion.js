import React from "react";
import { List } from "react-native-paper";
import ListItem from "./ListItem";

export default function ListAccordion({ accordion, id }) {
  return (
    <List.Accordion
      title={accordion.title}
      expanded={accordion.expanded}
      left={(props) => <List.Icon {...props} icon={accordion.leftIcon} />}
      onPress={() => accordion.onPress(accordion.id)}
    >
      {accordion.items.map((item) => (
        <ListItem key={item.id} item={item} parentId={accordion.id} />
      ))}
    </List.Accordion>
  );
}
