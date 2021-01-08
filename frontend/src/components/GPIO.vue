<template>
  <div>
    <table class="gpio-table" style="margin: 0 auto;">
      <tr>
        <td class="td-left"><GPIOPin :num="1" name="3V3" comment="POWER" label-position="left" color="#FC0" /></td>
        <td class="td-right"><GPIOPin :num="2" name="5V" comment="POWER" label-position="right" color="#F40" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="3" name="GPIO2" comment="SDA1 I2C" label-position="left" color="#F0F" /></td>
        <td class="td-right"><GPIOPin :num="4" name="5V" comment="POWER" label-position="right" color="#F40" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="5" name="GPIO3" comment="SCL1 I2C" label-position="left" color="#F0F" /></td>
        <td class="td-right"><GPIOPin :num="6" name="GROUND" comment="" label-position="right" color="#000" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="7" name="GPIO4" comment="" label-position="left" color="#084" /></td>
        <td class="td-right"><GPIOPin :num="8" name="GPIO14" comment="UART0_TXD" label-position="right" color="#808" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="9" name="GROUND" comment="" label-position="left" color="#000" /></td>
        <td class="td-right"><GPIOPin :num="10" name="GPIO15" comment="UART0_RXD" label-position="right" color="#808" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="11" name="GPIO17" comment="" label-position="left" color="#084" /></td>
        <td class="td-right"><GPIOPin :num="12" name="GPIO18" comment="PCM_CLK" label-position="right" color="#0CF" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="13" name="GPIO27" comment="" label-position="left" color="#084" /></td>
        <td class="td-right"><GPIOPin :num="14" name="GROUND" comment="" label-position="right" color="#000" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="15" name="GPIO22" comment="" label-position="left" color="#084" /></td>
        <td class="td-right"><GPIOPin :num="16" name="GPIO23" comment="" label-position="right" color="#084" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="17" name="3V3" comment="POWER" label-position="left" color="#FC0" /></td>
        <td class="td-right"><GPIOPin :num="18" name="GPIO24" comment="" label-position="right" color="#084" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="19" name="GPIO10" comment="SPI0_MOSI" label-position="left" color="#04F" /></td>
        <td class="td-right"><GPIOPin :num="20" name="GROUND" comment="" label-position="right" color="#000" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="21" name="GPIO9" comment="SPI0_MISO" label-position="left" color="#04F" /></td>
        <td class="td-right"><GPIOPin :num="22" name="GPIO25" comment="" label-position="right" color="#084" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="23" name="GPIO11" comment="SPI0_SCLK" label-position="left" color="#04F" /></td>
        <td class="td-right"><GPIOPin :num="24" name="GPIO8" comment="SPI0_CE0_N" label-position="right" color="#04F" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="25" name="GROUND" comment="" label-position="left" color="#000" /></td>
        <td class="td-right"><GPIOPin :num="26" name="GPIO7" comment="SPI0_CE1_N" label-position="right" color="#04F" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="27" name="ID_SD" comment="I2C EEPROM" label-position="left" color="#EE0" /></td>
        <td class="td-right"><GPIOPin :num="28" name="ID_SC" comment="I2C EEPROM" label-position="right" color="#EE0" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="29" name="GPIO5" comment="" label-position="left" color="#084" /></td>
        <td class="td-right"><GPIOPin :num="30" name="GROUND" comment="" label-position="right" color="#000" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="31" name="GPIO6" comment="" label-position="left" color="#084" /></td>
        <td class="td-right"><GPIOPin :num="32" name="GPIO12" comment="" label-position="right" color="#084" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="33" name="GPIO13" comment="" label-position="left" color="#084" /></td>
        <td class="td-right"><GPIOPin :num="34" name="GROUND" comment="" label-position="right" color="#000" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="35" name="GPIO19" comment="" label-position="left" color="#084" /></td>
        <td class="td-right"><GPIOPin :num="36" name="GPIO16" comment="" label-position="right" color="#084" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="37" name="GPIO26" comment="" label-position="left" color="#084" /></td>
        <td class="td-right"><GPIOPin :num="38" name="GPIO20" comment="" label-position="right" color="#084" /></td>
      </tr>
      <tr>
        <td class="td-left"><GPIOPin :num="39" name="GROUND" comment="" label-position="left" color="#000" /></td>
        <td class="td-right"><GPIOPin :num="40" name="GPIO21" comment="" label-position="right" color="#084" /></td>
      </tr>
    </table>
  </div>
</template>

<script>
  import GPIOPin from "./GPIOPin"

  export default {
    name: "GPIO",
    components: { GPIOPin },
  }
</script>

<style lang="scss" scoped>
  .gpio-table {
    td {
      padding: 4px;
    }
    .td-left {
      text-align: right;
    }
    .td-right {
      text-align: left;
    }
  }
</style>
