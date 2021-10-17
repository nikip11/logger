<template>
  <div @click="toUpperCase(2)">heelo</div>
</template>
<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

// export interface Message {

// }

export class Logger {
  getWindowsError(
    type: any,
    location: any,
    line: any,
    position: any,
    errorObj: any
  ) {
    console.log({ type, location, line, position, errorObj });
    // navigator.userAgent
    this.sendMessage("loggggg");
  }

  sendMessage(message: any) {
    console.log("send message: ", message);
    const xhr = new XMLHttpRequest();
    const formData = new FormData();
    formData.append("json", JSON.stringify(message));
    console.log("loggggg", xhr);

    // xhr.open("POST", process.env.VUE_APP_LOG_URL);
    xhr.open("POST", "http://127.0.0.1:5000/logs");
    // xhr.send(formData);
  }
}

Vue.config.errorHandler = (err, vm, info) => {
  // err: error trace
  // vm: component in which error occured
  // info: Vue specific error information such as lifecycle hooks, events etc.

  // TODO: Perform any custom logic or log to server
  console.error("Error occurred: ", { err, vm, info });
  // const logger = new Logger();
  // console.log(logger);
  // logger.sendMessage({ err, vm, info });
};

@Component
export default class LoggerComponent extends Vue {
  // @Prop() private msg!: Message;
  created() {
    // window.onerror = function(type, location, line, position, errorObj) {
    //   console.log({type, location, line, position, errorObj})
    //   const logger = new Logger()
    //   logger.getWindowsError(type, location, line, position, errorObj)
    // }
    // window.onerror = (type: any, location: any, line: any, position: any, errorObj: any) => {
    //   this.getWindowsError(type, location, line, position, errorObj)
    // }

    window.addEventListener("unhandledrejection", function (err) {
      if (err && err.reason) {
        let message =
          "Promise unhandled error" +
          " \nmessage: " +
          err.reason.message +
          " \n\nstack: " +
          err.reason.stack;
      }
      console.log("message error");
    });

    window.onerror = function (message, file, line, col, error) {
      console.log({ message, file, line, col, error });
      return false;
    };

    window.addEventListener("error", function (e) {
      console.log(e);
      return false;
    });
    const logger = new Logger();
    console.log(logger);
    const error = {
      err: "TypeError: Cannot read properties of undefined (reading 'map')at VueComponent.mounted",
      vm: "VueComponent",
      info: "mounted hook",
    };
    logger.sendMessage(error);
  }

  getWindowsError(
    type: any,
    location: any,
    line: any,
    position: any,
    errorObj: any
  ) {
    console.log({ type, location, line, position, errorObj });
    this.sendMessage("loggggg eeee");
  }

  sendMessage(message: string) {
    console.log("send message: ", message);
  }

  mounted() {
    // try {
    console.log("exit");
    const filter = {};
    // filter.mapper.map((item: any) => {
    //   console.log(item);
    // });
    // } catch (error) {
    //   throw true;
    // }
  }

  toUppercase(str: string) {
    if (typeof str !== "string") {
      throw TypeError("Wrong type given, expected a string");
    }
    return str.toUpperCase();
  }
}
</script>
