import React from "react";
import { View, Text, Alert } from "react-native";
import { List, Paragraph, Dialog, Portal } from "react-native-paper";
import Loading from "./Loading";
import ListAccordion from "../components/ListAccordion";
import { CustomContext } from "../contexts/CustomContext";

export default class HomeScreen extends React.Component {
  static contextType = CustomContext;

  constructor(props) {
    super(props);

    this.state = {
      isLoading: true,
      lists: this.testData(),
      isLogin: false,
    };
  }

  testData() {
    const today = new Date();
    const tom = new Date();
    tom.setDate(tom.getDate() + 1);

    heartIcon = {
      pressedIcon: "heart",
      unPressedicon: "heart-outline",
    };

    return (lists = [
      {
        id: 1,
        title: today.toLocaleDateString(),
        expanded: true,
        leftIcon: "folder",
        onPress: this.handlePress,
        items: [
          {
            id: 1,
            title: "삼성전자 배당락",
            description: "주가에 악영향 예상",
            leftIcon: { icon: "thumb-down", color: "blue" },
            rightIcon: {
              ...heartIcon,
              isPressed: false,
              onPress: this.listItemHeartOnPress,
            },
          },
          {
            id: 2,
            title: "LG전자 공시",
            description: "주가에 긍정적인 영향 예상",
            leftIcon: { icon: "thumb-up", color: "red" },
            rightIcon: {
              ...heartIcon,
              isPressed: true,
              onPress: this.listItemHeartOnPress,
            },
          },
        ],
      },
      {
        id: 2,
        title: tom.toLocaleDateString(),
        expanded: false,
        leftIcon: "folder",
        onPress: this.handlePress,
        items: [
          { id: 1, title: "테스트용 내용" },
          { id: 2, title: "테스트내용2" },
          { id: 3, title: "테스트내용3" },
        ],
      },
    ]);
  }

  handlePress = (id) => {
    const { lists } = this.state;
    this.setState({
      lists: lists.map((accordion) =>
        accordion.id === id
          ? { ...accordion, expanded: !accordion.expanded }
          : accordion
      ),
    });
  };

  listItemHeartOnPress = (accordionId, itemId) => {
    const { lists, isLogin } = this.state;
    const { navigation } = this.props;

    if (!isLogin) {
      Alert.alert("로그인", "로그인하셔야 이용가능합니다.", [
        {
          text: "취소",
          onPress: () => console.log("Cancel Pressed"),
          style: "cancel",
        },
        { text: "로그인하기", onPress: () => navigation.navigate("Login") },
      ]);
      return;
    }

    this.setState({
      lists: lists.map((accordion) =>
        accordion.id === accordionId
          ? {
              ...accordion,
              items: accordion.items.map((item) =>
                item.id === itemId
                  ? {
                      ...item,
                      rightIcon: {
                        ...item.rightIcon,
                        isPressed: !item.rightIcon.isPressed,
                      },
                    }
                  : item
              ),
            }
          : accordion
      ),
    });
  };

  componentDidMount() {
    this.setState({ isLoading: false, isLogin: this.context.state.isLogin });
  }

  render() {
    const { isLoading, lists } = this.state;
    return isLoading ? (
      <Loading />
    ) : (
      // <List.Section title="관련일자">
      lists.map((accordion) => (
        <ListAccordion
          key={accordion.id}
          accordion={accordion}
          onPress={this.handlePress}
        />
      ))
      // </List.Section>
    );
  }
}
