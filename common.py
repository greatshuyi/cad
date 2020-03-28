# -*- coding: utf-8 -*-

from enum import Enum
from abc import abstractmethod

from prga.arch.ds import DSTreeNode


class BaseArchTag(DSTreeNode):
    pass


class NodeType(Enum):
    SINK = 1
    SOURCE = 2
    CONSTANT = 3        #(VDD, VCC, GND port .etc)


class PortType(Enum):
    CLOCK = 1
    SYNC_RESET = 2
    ASYNC_RESET = 3
    NORMAL = 4
    VDD = 5
    VCC = 6
    GND = 7



class PortDirection(Enum):
    IN = 0
    OUT = 1
    INOUT = 2


class Item(object):
    pass


class Port(Item):

    __slots__ = ['name', 'direction', 'types', 'props']

    def __init__(self, name: str,
                       direction: PortDirection,
                       types: PortType,
                       **props):
        self.name = name
        self.direction = direction
        self.types = types
        self.props.update(props)

    @property
    def is_input(self):
        return self.direction == PortDirection.IN

    @property
    def is_output(self):
        return self.direction == PortDirection.OUT

    @property
    def is_inout(self):
        return self.direction == PortDirection.INOUT

    @property
    def is_clock(self):
        return self.name == PortType.CLOCK

    @property
    def is_sync_reset(self):
        return self.name == PortType.SYNC_RESET

    @property
    def is_sync_reset(self):
        return self.name == PortType.ASYNC_RESET

    @property
    def clock_domain(self):
        """Which clock domain current port belongs to"""
        return self.props.get("clock_domain", None)

    @property
    def is_sync_port(self):
        return self.clock_domain.is_clock

    def __repr__(self):
        return "{}".format(self.name)

    def __str__(self):
        return "{}".format(self.name)

    def __hash__(self):
        return hash(self.name+str(id(self)))

    def __eq__(self, other):
        return isinstance(other, Port) and id(other) == id(self)

    def __ne__(self, other):
        return not self == other

    # TODO: implement
    @abstractmethod
    def render(self):
        """
        Return a xml represented tag
        :return:
        """
        pass


class ModelPort(Port):

    def render(self):
        pass

class BlockPort(Port):

    @property
    def is_non_clock_global(self):
        pass

    def render(self):
        pass


class Arc(object):
    pass


class Model(BaseArchTag):

    def __init__(self, name):
        self.name = name
        self.iports = []
        self.oports = []
        self._validated = False

    def __getitem__(self, item):
        ports = self.iports + self.oports
        p = next(filter(lambda x: x == item, ports), None)
        if p is None:
            raise KeyError
        else:
            return p

    def __contains__(self, item):
        try:
            _ = self.__getitem__(item)
            return True
        except KeyError:
            return False

    def create_clock(self, name):
        if self.__contains__(name):
            raise KeyError("clock port {} already exists".foramt(name))
        clk = ModelPort(name, PortDirection.IN, PortType.CLOCK)
        self.iports.append(clk)
        self._validated = False
        return clk

    def create_port(self, name:str, direction:PortDirection):
        if self.__contains__(name):
            raise KeyError("port {} already exists".foramt(name))
        port = ModelPort(name, direction, PortType.NORMAL)
        return port

    def relate_clock(self, port, clock):
        if not self.__contains__(port):
            raise KeyError("port {} already exists".foramt(port))

        if clock is not None or "":
            if not self.__contains__(clock):
                raise KeyError("clock port {} does not created, create clock port first".format(clock))



    def connect_port(self, start, end):
        pass



    def validate(self):
        # check port's name uniqueness

        # check topological connection

        # last step to set validated
        self._validated = True

    def render(self):
        self.validate()
        # actual rendering



    @property
    def inputs(self):
        return [p.name for p in self.iports if not p.clock]

    @property
    def outputs(self):
        return [p.name for p in self.oports]

    @property
    def clocks(self):
        return [p.name for p in self.iports if p.clock]

    @property
    def ports(self):
        """Return a list of all ports' name"""
        iname = self.inputs
        oname = self.outputs
        clock = self.clocks
        name = iname + oname + clock
        return name

    @property
    def validated(self):
        return self._validated

    @property
    def as_graph(self):
        pass





class ArchModels(object):
    """
    <models>
        <model name="single_port_ram">
            <input_ports>
              <port name="we" clock="clk" />
              <port name="addr" clock="clk" combinational_sink_ports="out"/>
              <port name="data" clock="clk" combinational_sink_ports="out"/>
              <port name="clk" is_clock="1"/>
            </input_ports>
        <output_ports>
            <port name="out" clock="clk"/>
            </output_ports>
        </model>

        <model name="adder">
            <input_ports>
                <port name="a" combinational_sink_ports="cout sumout"/>
                <port name="b" combinational_sink_ports="cout sumout"/>
                <port name="cin" combinational_sink_ports="cout sumout"/>
            </input_ports>
            <output_ports>
                <port name="cout"/>
                <port name="sumout"/>
            </output_ports>
        </model>
    </models>
    """



    @classmethod
    def create_model(cls, name: str):
        """Return a default arch.model tag definition
        :param name:
        :return:
        """
        m = Model(name)



class BlockPrimitiveClass(Enum):



class Block(DSTreeNode, Item):



    def __init__(self, name, num, blif=None, cls=None):
        super(Block, self).__init__()

