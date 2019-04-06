import panda3d.core as p3d


class RenderPass:
    def __init__(
            self,
            name,
            pipe=None,
            engine=None,
            window=None,
            camera=None,
            scene=None,
            shader=None,
            clear_color=p3d.LColor(0.41, 0.41, 0.41, 0.0)
    ):
        self.name = name
        self._pipe = pipe if pipe else base.pipe
        self._engine = engine if engine else base.graphics_engine
        self._window = window if window else base.win
        self._root = p3d.NodePath(p3d.ModelNode(f'{self.name}_root'))
        if scene:
            scene.instance_to(self._root)
        if shader:
            self._root.set_shader(shader)

        self._camera = self._make_camera(camera)
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


    def _make_camera(self, source_cam):
        cam = p3d.Camera(f'{self.name}_camera')
        cam_nodepath = self._root.attach_new_node(cam)
        cam.set_scene(self._root)

        if source_cam:
            def update(callback_data):
                try:
                    lens = source_cam.get_node(0).get_lens()
                except AttributeError:
                    lens = source_cam.find('**/+Camera').get_node(0).get_lens()
                cam.set_lens(lens)
                cam_nodepath.set_pos(source_cam.get_pos(self._root))
                cam_nodepath.set_hpr(source_cam.get_hpr(self._root))
                callback_data.upcall()
            callback = p3d.CallbackNode(f'{self.name}_update_camera')
            callback.set_cull_callback(update)
            cam_nodepath.attach_new_node(callback)

        return cam_nodepath

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
