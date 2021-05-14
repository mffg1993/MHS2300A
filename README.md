# MHS2300A

A simple Python module to control the inexpensive MHS2300A signal generator. 


## What is it for? 

Affordable signal generators have allowed to the maker community to build their own electrocnic laboratory. In particular, the MHS2300A represents an entry-level test and measurement equipment for electronic engineers, electronic laboratories, production lines and teaching and scientific research. The MHS2300A has two channels with multiple tunable parameters that can be changed using the built-in button functions but there is the possibility of controlling it from a computer using the right protocol. However, one compromise I have encountered is that we are limited to the GUI provided by the company. Here, I present a module to control this signal generator with Python. 

## Requirements
 
- Pyserial and Cached_property packages need to be installed 

## Installation


```python
pip install mhs2300a
```

## Examples of usage

First, we import the MHS2300 module


```python
from mhs2300a import MHS2300
```

Then, we create the object that handles the Signal Generator. For that, we need to specify the serial port we are going to use:
- Windows: COM_ 
- Linux:  /dev/ttyUSB0


```python
port_name = "COM3" 
signal = MHS2300(port_name)
```

By default, the signal generator enable both channels. We can enable or disable each channel independently using the built-in methods **on** or **off** and specifying the channel.  


```python
# Enables on channel 2 
signal.on(2) 


# Disables channel 1 
signal.off(1) 
```

Similarly, it is possible to modify each of the following parameters: 

- Amplitude 
- Frequency
- Phase 
- Offset
- Duty


```python
# Sets the amplitude of the channel 2 to 5 Volts
signal.Amplitude(2,5) 

# Sets the frequency of the channel 2 to 5 Hertz
signal.Frequecy(2,5)

# Sets the phase of the channel 2 to 10
signal.Phase(2,10)

# Sets the phase of the channel 1 to 5% 
signal.Offset(1,5)

# Sets the phase of the channel 1 to 3
signal.Duty(1,3)
```

We can close the communication with the signal generator


```python
signal.port.close()
```
