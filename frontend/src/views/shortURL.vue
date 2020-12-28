<template>
  <div class="animated fadeIn" style="padding: 10px 10px 10px 10px">
    <CRow>
      <CCol sm="12" align="center">
        <h2>歡迎使用縮網址</h2>
        <CInput
          v-model="input_url"
          placeholder="在這裡輸入你的網址"
          style="width: 60%; display: inline-block"
        />
        <CButton
          color="success"
          size="lg"
          style="width: auto; display: inline-block"
          @click="shortButton()"
          >縮址</CButton
        >
        <h4 style="color: red">{{ error_msg }}</h4>
        <br />
        <br />
        <CCard style="width: 50%">
          <CCardHeader> 你的縮網址為 </CCardHeader>
          <CCardBody>
            {{ new_url }}
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  </div>
</template>

<script>
import { freeSet } from "@coreui/icons";
export default {
  name: "shortURL",
  freeSet,

  data() {
    return {
      input_url: "",
      new_url: "",
      error_msg: "",
    };
  },

  methods: {
    shortButton() {
      this.new_url = "";
      this.error_msg = "";
      this.input_url = this.input_url.trim();
      var rules = /(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/ ~\+#]*[\w\-\@?^=%&/~\+#])?/;
      if (this.input_url == "") {
        return;
      } else if (rules.test(this.input_url)) {
        let param = { old_url: this.input_url };
        this.$http.post("http://localhost:8000/shortUrl", param).then((res) => {
          this.new_url = res.data.new_url;
          console.log(this.new_url);
        });
      } else {
        this.error_msg = "請注意這不是合法的網址";
      }
    },
  },
};
</script>
