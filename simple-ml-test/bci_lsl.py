import uuid

from pylsl import StreamInlet, resolve_byprop


class LslBciConnection:

    def __init__(self, stream_name) -> None:
        super().__init__()

        self.uuid = uuid.uuid4()
        self.resolve_stream_in_process = False
        self.stream_name = None
        self.stream = None
        self.inlet = None

        if not stream_name:
            raise Exception("Stream name can not be empty or None!")
        else:
            self.stream_name = stream_name

    def __hash__(self):
        return hash(self.uuid)

    def __eq__(self, other):
        if isinstance(other, LslBciConnection):
            return self.uuid == other.uuid
        else:
            return False

    def resolve_stream(self):
        self.resolve_stream_in_process = True
        try:
            streams = resolve_byprop('name', self.stream_name, timeout=10)
        finally:
            self.resolve_stream_in_process = False
        self.stream = streams[0]
        self.inlet = StreamInlet(self.stream, recover=False)
        self.resolve_stream_in_process = False

    def get_sample(self):
        if not self.inlet:
            raise Exception("Stream is not resolved!")

        sample, _ = self.inlet.pull_sample()
        return sample

    def close_stream(self):
        self.inlet.close_stream()
