<template>
  <v-container fluid class="mb-10">
    <v-card elevation="0" color="transparent">
      <v-row justify="center">
        <v-col cols="12" sm="12" class="text-truncate text-center">
          <v-card outlined :color="buttonText ? '' : 'transparent'" :elevation="buttonText ? '1' : '0'">
            <v-row justify="center">
              <v-col v-if="url" cols='12' sm='12'>
                  <img
                    :src="url"
                    style="max-width: 100%; max-height: 300px"
                    aspect-ratio=".64"
                    cover
                  />
              </v-col>
              <v-col cols='12' sm='12' class="align-center">
                 <input
                ref="uploader"
                class="d-none"
                type="file"
                accept="image/*"
                @change="onFileChanged"
              />
              </v-col>
              <v-col cols='12' sm='12' class="align-center">
                  <v-btn @click="done">done</v-btn>
                  <v-btn
                  @click="cancel"
                  class="ma-1" 
                  dark 
                  color='red'>
                    <b>cancel</b>
                  </v-btn>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
  import axios from 'axios'
export default {
  name: "Similarity",
  data: () => ({
    tabs: null,
    defaultButtonText: "",
    selectedFile: null,
    isSelecting: false,
    url: null
  }),
  computed: {
    buttonText() {
      return this.selectedFile
        ? this.selectedFile.name
        : this.defaultButtonText;
    }
  },
  methods: {
    onButtonClick() {
      this.isSelecting = true;
        window.addEventListener("focus",() => {this.isSelecting = false;},
        { once: true }
      );
      this.$refs.uploader.click();
    },
    onFileChanged(e) {
      this.selectedFile = e.target.files[0];
      this.url = URL.createObjectURL(this.selectedFile);
    },
    done(){
      const formData = new FormData()
      formData.append('image_url', this.url)
      formData.append('data', this.selectedFile)

      axios.post('http://127.0.0.1:5000/',formData)
      .then((response) => {
        console.log("here", response);
      }), 201
    },
    cancel(){
      this.defaultButtonText= ""
      this.selectedFile= null
      this.isSelecting= false
      this.url= null
    }
  }
};
</script>