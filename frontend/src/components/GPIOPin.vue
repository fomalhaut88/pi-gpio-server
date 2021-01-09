<template>
  <div>
    <div class="pin-label" v-if="labelPosition == 'left'">
      <div class="has-text-weight-bold">{{ name }}</div>
      <div class="has-text-grey">{{ comment }}</div>
    </div>

    <div class="pin-itself" :style="{'border-color': color}" @click="editModalOpen()">{{ num }}</div>

    <div class="pin-label" v-if="labelPosition == 'right'">
      <div class="has-text-weight-bold">{{ name }}</div>
      <div class="has-text-grey">{{ comment }}</div>
    </div>

    <b-modal class="has-text-left" ref="editModal" v-model="isEditModal">
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">Pin {{ num }} ({{ name }})</p>
          <button type="button" class="delete" @click="$refs.editModal.close()"/>
        </header>
        <section class="modal-card-body">
          <div class="columns">
            <div class="column">
              <b-field label="Direction">
                <b-radio-button v-model="direction" native-value="out" type="is-info" @change="changeDirection()">
                    Output
                </b-radio-button>
                <b-radio-button v-model="direction" native-value="in" type="is-warning" @change="changeDirection()">
                    Input
                </b-radio-button>
              </b-field>
            </div>
            <div class="column">
              <div v-if="direction == 'out'">
                <b-field label="Set value">
                  <b-radio-button v-model="value" :native-value="0" type="is-black">
                      <strong>0</strong>
                  </b-radio-button>
                  <b-radio-button v-model="value" :native-value="1" type="is-success">
                      <strong>1</strong>
                  </b-radio-button>
                </b-field>
              </div>
              <div v-else>
                <div class="has-text-weight-bold">Value</div>
                <div class="has-text-weight-bold is-size-3" :class="{'has-text-success': value == 1, 'has-text-black': value == 0}">{{ value }}</div>
              </div>
            </div>
          </div>
        </section>
        <footer class="modal-card-foot">
          <button class="button" type="button" @click="$refs.editModal.close()">Close</button>
        </footer>
      </div>
    </b-modal>
  </div>
</template>

<script>
  const GPIO_PIN_TIMEOUT = parseInt(process.env.VUE_APP_GPIO_PIN_TIMEOUT)

  export default {
    name: "GPIOPin",
    props: {
      num: Number,
      name: String,
      comment: String,
      labelPosition: {
        type: String,
        default: "right",
      },
      color: {
        type: String,
        default: "#000",
      },
    },
    data() {
      return {
        isEditModal: false,
        direction: 'out',
        value: 0,
        pinsResource: this.$resource('pins{/id}'),
        valueInterval: null,
      }
    },
    watch: {
      direction: function(value) {
        this.pinsResource.save({id: this.num}, { direction: value }).then(() => {
          this.performValueInterval()
          if (value == 'out') {
            this.value = 0
          }
        })
      },
      value: function(value) {
        this.pinsResource.save({id: this.num}, { value })
      },
    },
    methods: {
      editModalOpen() {
        if (this.name.substring(0, 4) == 'GPIO') {
          this.isEditModal = true
        }
      },
      performValueInterval() {
        if (this.direction == 'in') {
          if (this.valueInterval === null) {
            this.valueInterval = setInterval(() => {
              this.pinsResource.get({id: this.num}).then(response => {
                this.value = response.data.value
              })
            }, GPIO_PIN_TIMEOUT)
          }
        } else {
          if (this.valueInterval !== null) {
            clearInterval(this.valueInterval)
            this.valueInterval = null
          }
        }
      },
    },
    mounted() {
      this.pinsResource.get({id: this.num}).then(response => {
        this.direction = response.data.direction
        this.value = response.data.value
        this.performValueInterval()
      })
    },
  }
</script>

<style lang="scss" scoped>
  .pin-label {
    display: inline-block;
    margin: 0 8px;
    position: relative;
    top: 6px;

    div {
      display: block;
      line-height: 16px;
      font-size: 14px;

      &:empty::after {
        content: " ";
        white-space: pre;
      }
    }
  }

  .pin-itself {
    display: inline-block;
    border-radius: 2rem;
    border-width: 6px;
    border-style: solid;
    width: 44px;
    height: 44px;
    line-height: 32px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    cursor: pointer;

    &:hover {
      opacity: 0.75;
    }
  }
</style>
