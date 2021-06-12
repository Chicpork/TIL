import React, { useRef } from "react";
import {
  View,
  Text,
  StyleSheet,
  KeyboardAvoidingView,
  Platform,
  Alert,
} from "react-native";
import { TextInput, Button, HelperText } from "react-native-paper";
import { CustomContext } from "../contexts/CustomContext";

export default function LoginScreen({ navigation }) {
  const [isLoading, setIsLoading] = React.useState(false);
  const [isEmailValid, setIsEmailValid] = React.useState(true);
  const [isPasswordValid, setIsPasswordValid] = React.useState(true);
  const [inputs, setInputs] = React.useState({ email: "", password: "" });

  const {
    state: { isTest },
    stateAction: { testSignIn, signIn },
  } = React.useContext(CustomContext);

  const emailInput = useRef();
  const passwordInput = useRef();

  const { email, password } = inputs;

  function validateEmail(email) {
    var re =
      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    return re.test(email);
  }

  const loginRequest = async (email, password) => {
    try {
      await signIn(email, password);

      navigation.popToTop(); //메인화면으로 이동
    } catch (error) {
      console.log(error);
      if (error.hasOwnProperty("loginFail")) {
        Alert.alert("로그인 실패", error.loginFail);
      } else {
        Alert.alert("로그인 실패", "알수없는 오류입니다.");
      }
      setIsLoading(false);
    }
  };

  function login() {
    console.log(email, password);

    const isEmailValid = validateEmail(email);
    if (!isEmailValid) {
      emailInput.current.focus();
      setIsLoading(false);
      setIsEmailValid(isEmailValid);
      return;
    }

    const isPasswordValid = password.length >= 8;
    if (!isPasswordValid) {
      passwordInput.current.focus();
      setIsLoading(false);
      setIsPasswordValid(isPasswordValid);
      return;
    }

    setIsLoading(true);

    if (isTest) {
      testSignIn("test");
      setIsLoading(false);
      navigation.popToTop();
    } else {
      loginRequest(email, password);
    }
  }

  React.useEffect(() => {}, []);

  return (
    <View style={styles.container}>
      <View style={styles.titleContainer}>
        <Text style={styles.titleText}>Login TEST</Text>
      </View>
      <KeyboardAvoidingView
        style={styles.innerContainer}
        behavior={Platform.OS === "ios" ? "padding" : "height"}
      >
        <TextInput
          mode="outlined"
          left={
            <TextInput.Icon
              name="email"
              color="rgba(0, 0, 0, 0.38)"
              size={25}
              style={{ backgroundColor: "transparent" }}
            />
          }
          value={email}
          keyboardAppearance="light"
          autoCapitalize="none"
          autoCorrect={false}
          keyboardType="email-address"
          returnKeyType="next"
          blurOnSubmit={true}
          placeholder={"Email"}
          ref={emailInput}
          onSubmitEditing={() => passwordInput.current.focus()}
          onChangeText={(email) => {
            setIsEmailValid(true);
            setInputs({ ...inputs, email });
          }}
          style={styles.textInput}
          error={!isEmailValid}
        />
        <HelperText
          type="error"
          visible={!isEmailValid}
          style={{ display: isEmailValid ? "none" : "flex" }}
        >
          이메일 형식이 맞는지 확인하세요.
        </HelperText>
        <TextInput
          mode="outlined"
          left={
            <TextInput.Icon
              name="lock"
              color="rgba(0, 0, 0, 0.38)"
              size={25}
              style={{ backgroundColor: "transparent" }}
            />
          }
          value={password}
          keyboardAppearance="light"
          autoCapitalize="none"
          autoCorrect={false}
          secureTextEntry={true}
          returnKeyType="done"
          blurOnSubmit={true}
          placeholder={"Password"}
          ref={passwordInput}
          onSubmitEditing={() => login()}
          onChangeText={(password) => {
            setIsPasswordValid(true);
            setInputs({ ...inputs, password });
          }}
          style={styles.textInput}
          error={!isPasswordValid}
        />
        <HelperText
          type="error"
          visible={!isPasswordValid}
          style={{ display: isPasswordValid ? "none" : "flex" }}
        >
          이메일 형식이 맞는지 확인하세요. 비밀번호는 최소 8자리입니다.
        </HelperText>
        <Button
          mode="contained"
          onPress={login}
          labelStyle={styles.loginTextButton}
          loading={isLoading}
          disabled={isLoading}
          style={styles.loginButton}
        >
          LOGIN
        </Button>
      </KeyboardAvoidingView>
      <View style={styles.helpContainer}>
        <Button
          mode="text"
          labelStyle={{ color: "white" }}
          style={{ backgroundColor: "transparent" }}
          contentStyle="transparent"
          onPress={() => console.log("Account created")}
        >
          Need help?
        </Button>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  titleContainer: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    // marginBottom: 48,
    backgroundColor: "red",
  },
  innerContainer: {
    flex: 3,
    justifyContent: "flex-start",
    alignItems: "center",
    backgroundColor: "yellow",
  },
  helpContainer: {
    flex: 1,
    alignItems: "center",
    backgroundColor: "green",
  },
  textInput: {
    width: "90%",
    marginBottom: 20,
  },
  loginButton: {
    width: "90%",
  },
  titleText: {
    color: "black",
    fontSize: 30,
  },
  loginContainer: {
    alignItems: "center",
    justifyContent: "center",
  },
});
