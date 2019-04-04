import panda3d.core as p3d


class RenderPass:
    def __init__(
            self,
            name,
            pipe=None,
            engine=None,
            window=None,
            camera=None,
            clear_color=p3d.LColor(0.41, 0.41, 0.41, 0.0)
    ):
        self.name = name
        self._pipe = pipe if pipe else base.pipe
        self._engine = engine if engine else base.graphics_engine
        self._window = window if window else base.win
        self._camera = camera
        self.output = p3d.Texture(f'{self.name}_output')
        self.buffer = self._make_buffer()

        self.buffer.add_render_texture(
            self.output,
            p3d.GraphicsOutput.RTM_bind_or_copy,
            p3d.GraphicsOutput.RTP_color
        )

        self.display_region = self.buffer.make_display_region(0, 1, 0, 1)
        if self._camera:
            self.display_region.set_camera(self._camera)
        self.buffer.set_clear_color(clear_color)

    def _make_buffer(self):
        fb_props = p3d.FrameBufferProperties()
        fb_props.set_rgba_bits(8, 8, 8, 0)
        fb_props.set_depth_bits(24)

        return self._engine.make_output(
            self._pipe,
            self.name,
            0,
            fb_props,
            p3d.WindowProperties(),
            p3d.GraphicsPipe.BF_refuse_window | p3d.GraphicsPipe.BF_size_track_host,
            self._window.get_gsg(),
            self._window
        )
