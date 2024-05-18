from decimal import Decimal
from dataclasses import dataclass, field

@dataclass
class ComponentData:
    name: str
    flowrate: Decimal

@dataclass
class StreamData:
    name: str
    components: dict[str, ComponentData] = field(default_factory=dict)

@dataclass
class UnitData:
    name: str
    input_streams: dict[str, StreamData] = field(default_factory=dict)
    output_streams: dict[str, StreamData] = field(default_factory=dict)

# Example
component_dict_stream1 = { 'A': ComponentData('A', Decimal(1.5)) }
component_dict_stream2 = { 'B': ComponentData('B', Decimal(2.3)) }
component_dict_stream3 = { 'B': ComponentData('B', Decimal(2.3)) }

input_stream_dict_unit = {
    'Stream 1': StreamData('Stream 1', components=component_dict_stream1),
    'Stream 2': StreamData('Stream 2', components=component_dict_stream2),
    'Stream 3': StreamData('Stream 2', components=component_dict_stream3),
}

unit_1: UnitData = UnitData('Unit', input_streams=input_stream_dict_unit)

def calculate_process_outputs(unit: UnitData):
    output_stream: StreamData = StreamData(name='Output')

    for stream in unit.input_streams.values():
        for component in stream.components.values():
            if component.name not in output_stream.components:
                output_stream.components[component.name] = ComponentData(name=component.name, flowrate=component.flowrate)
            else:
                output_stream.components[component.name].flowrate += component.flowrate
    
    unit.output_streams[output_stream.name] = output_stream

    print(unit)
    print(unit.output_streams['Output'].components['A'].flowrate)
    print(unit.output_streams['Output'].components['B'].flowrate)

calculate_process_outputs(unit_1)