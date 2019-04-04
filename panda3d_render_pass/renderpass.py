import panda3d.core as p3d


def create_default_framebuffer_properties():
    props = p3d.FrameBufferProperties()
    props.set_rgba_bits(8, 8, 8, 0)
    props.set_depth_bits(24)
    return props


def create_window_properties(size_x, size_y):
    return p3d.WindowProperties.size(size_x, size_y)

def create_buffer(name, pipe, engine, window):
    return engine.make_output(
        pipe,
        name,
        0,
        create_default_framebuffer_properties(),
        p3d.WindowProperties(),
        p3d.GraphicsPipe.BF_refuse_window | p3d.GraphicsPipe.BF_size_track_host,
        window.get_gsg(),
        window
    )

class RenderPass:
    def __init__(
            self,
            name,
            pipe=None,
            engine=None,
            window=None,
            camera=None,
    ):
        self.name = name
        self._pipe = pipe if pipe else base.pipe
        self._engine = engine if engine else base.graphics_engine
        self._window = window if window else base.win
        self._camera = camera if camera else base.cam
        self.output = p3d.Texture(f'{self.name}_output')
        self.buffer = create_buffer(
            self.name,
            self._pipe,
            self._engine,
            self._window
        )

        self.buffer.add_render_texture(
            self.output,
            p3d.GraphicsOutput.RTM_bind_or_copy,
            p3d.GraphicsOutput.RTP_color
        )

        self.display_region = self.buffer.make_display_region(0, 1, 0, 1)
        self.display_region.set_camera(self._camera)
