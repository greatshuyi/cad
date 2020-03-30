[WaveDrom: Open source timing diagram, register definition and circuit diagram](https://wavedrom.com/) with usage [paper](https://wavedrom.com/images/SNUG2016_WaveDrom.pdf) with some example:

Circuit:

    {assign:[
                ["g0", ["^", "b0", "b1"]],
                ["g1", ["^", "b1", "b2"]],
                ["g2", ["^", "b2", "b3"]],
                ["g3", ["=", "b3"]]
            ]
     }


Bit field diagram:

    {reg: [
            {bits: 8, name: 'IPO', attr: 'RO'},
            {bits: 7},
            {bits: 5, name: 'BRK', attr: 'RW'},
            {bits: 1, name: 'CPK'},
            {bits: 3, name: 'Clear'},
            {bits: 8}
          ]
    }


