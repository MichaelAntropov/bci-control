# P300 Region Study (OpenBCI)

The aim of this document is to describe how sensors are relocated in Open BCI helmet,
from 10-20 system to custom locations.
It is done in order to get more readings/data for P300 experement.

## Sensor relocation

#### Original locations:

If the assembly of OpenBCI Ultracortex Mk4 helmet was done following this [guide](https://docs.openbci.com/AddOns/Headwear/MarkIV/) then the helmet should have electrodes located in 10-20 system
(assuming 16-channel version was assembled):

![Electrodes Locations](../bci-occipital-sensor-reposition/media/electrode_locations.jpg)

When streamed with LSL protocol, the streamed data has the following order:
```
['fp1','fp2','c3','c4','p7','p8','o1','o2','f7','f8','f3','f4','t7','t8','p3','p4']
```

It is important since we will be moving sensors and will have to 'relabel' channels.

#### Relocating sensors:

The new location of the sensors will be moved as follows:

| Original |    | New | Ch No. |   |
|:--------:|:--:|:---:|:------:|:-:|
|    T8    | -> | Oz  |   14   |   |
|    O1    | -> | Po5 |   7    |   |
|    O2    | -> | Po6 |   8    |   |
|    T7    | -> | Pz  |   13   |   |
|    F4    | -> | Fz  |   12   |   |
|    F3    | -> | Cz  |   11   |   |

 When streamed with LSL protocol, the streamed data has the following order:

```
['fp1', 'fp2', 'po3', 'po4', 'p7', 'p8', 'po5', 'po6', 'f7', 'f8', 'Cz', 'Fz', 'Pz', 'Oz', 'p3', 'p4']
```

The indexes(0-based) of channels that we need for P300:

```
[10, 11, 12, 13]
```

### Testing relocation

Testing can be done with [OpenBCI GUI Impedance Test](https://docs.openbci.com/Software/OpenBCISoftware/GUIDocs/#impedance-testing)