# ButtonBox

## Aim

The aim of this device was to have something that can easily use to interface with other small projects, such as this  [Servo Robot Arm](https://ls.codetech.nl/shops/346407/files/420569260/otronic-robot-arm-exclusief-servomotors.jpg).

At its core, a ButtonBox (or 'Job Agnostic Button Box', as it's full title is), is a collection of input and output devices all hooked up to a single microcontroller. The microcontroller has some standard libraries and functions for operating those inputs and outputs, and is easily accessible for extending its software. Connecting the box to other devices can be done via common connectors such as USB or jackplugs. Down below is described in more detail what this specific box is made of, but in reality these details don't matter too much. The important idea is to have convenient input, output, and extensibility.

## Shopping list

### Core & Power

[Box (100x60x25mm)](https://www.amazon.nl/dp/B0BWLR5D1G?psc=1&ref=ppx_yo2ov_dt_b_product_details)

[Raspberry Pi Pico W](https://www.kiwi-electronics.com/nl/raspberry-pi-pico-w-10938?search=pi%20pico%20w)

[DC power jack](https://www.otronic.nl/nl/dc-power-jack-female-55x21mm-dc-022-met-moer.html)

[Step-down buck converter](https://www.otronic.nl/nl/step-down-buck-converter-van-45v-24v-naar-5v-3a-4r.html)

[1N4001 rectifier diodes (2)](https://www.kiwi-electronics.com/nl/1n4001-diode-10-stuks-395?search=diode)

### On front

[SPST on-off tilt switch](https://www.amazon.nl/Tuimelschakelaar-Posities-Voertuig-Dashboard-donkerblauw/dp/B0B56S4F1X/ref=sr_1_8?crid=3L6O8K6EK71SE&dib=eyJ2IjoiMSJ9.v541vdw9z-Gsqdh63qAZiGlg7uDVmMBUlbHnGP08O9RVf6p69ldrgtE4g8KSn__hcIeClaAKK7l0NInLeZSTqhHTJH_CTCyFxiU86x4GiNtJAcv-CBNYzTlAGA8MGanajAq-M7Wx2oSaMFku316TlYI3Jl63k6DqbG3dl0X_E35wuIV5jSb1N-itHESdDXuHGwFZfaqp0tnV1S0dEGDBXrJOz8KWfNPMw6UnDviX2oBF_mWYNg1REdci168dECjyM3zp5A3axiMomMmJssktsKRl_-8XIAT4jtMP7ecEo7A.5pwQPmhQj2k5DSSFwV4-vspxP1Y051O7QYNprQhyL3c&dib_tag=se&qid=1714934226&sprefix=spst,aps,103)

[SPDT on-off-on tilt switches (2)](https://www.amazon.nl/dp/B07SPYDVKH?psc=1&ref=ppx_yo2ov_dt_b_product_details)

### On top

[Mini OLED display 128x64 I2C](https://www.otronic.nl/nl/mini-oled-display-geel-blauw-096-inch-128x64-i2c.html)

[Joystick](https://www.otronic.nl/nl/joystick-module.html)

[Rotary encoder KY-040](https://www.amazon.nl/dp/B07T3672VK?psc=1&ref=ppx_yo2ov_dt_b_product_details)

### IO connectors

[Mini jack TRRS connectors (2)](https://www.amazon.nl/dp/B089222S84?psc=1&ref=ppx_yo2ov_dt_b_product_details) (with [male plugs](https://www.amazon.nl/dp/B0C276YP29?psc=1&ref=ppx_yo2ov_dt_b_product_details) for the other side)

[USB-C connector](https://www.amazon.nl/dp/B0BB68QYV9?psc=1&ref=ppx_yo2ov_dt_b_product_details)

### Etc

Spacers, screws, (dupont) wires, shrinkwrap, etc. 

## Building

A few things to keep in mind when building:

- Plan the joystick connection early on. The Pico has three accessible ADC pins, and the joystick needs two of them (for x and y axis). 
- Other than that, the precise pin-layout of the build isn't too important. Connect your devices wherever is convenient, and adjust the pins in the corresponding Python modules. 
- A step-down buck converter isn't strictly necessary, as long as you can be sure that you're only ever supplying 5V. In the current build, the converter is there as a safety net: you can accidentally attach higher voltages without frying the system. 
- Use diodes to keep the current flowing in one direction only. This is useful for when it's connected to both external power, and via the micro-USB of the Pico. 
- There is also a diode from the buck converter to the USB-C port, since in this build the 5V of the USB-C is only used to power an external device, not to power the Pico. 


## Future plans

I plan to use the buttonbox with other electronics projects, such as the aforementioned robot arm. I will update the code accordingly. 

The 'main' branch will remain fairy agnostic to what the box is actually doing, but I will update it with useful bits and pieces. Some obvious enhancement will be the inclusion of WiFi and BlueTooth capabilities. 

## Inspiration

During the build I was deeply inspired by the done manifesto, especially 'perfection is boring, it stops you from getting it done'.

![Cult of done](https://miro.medium.com/v2/resize:fit:720/format:webp/1*KOVbr0RTE7l60rft2dyclg.png)


