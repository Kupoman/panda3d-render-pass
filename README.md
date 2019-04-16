# Render Pass
This library is intended to make multi-pass rendering a little easier in Panda3D.
Each RenderPass objects represents a render target and a scene to render.
If no scene is given, a fullscreen quad is rendered.
This library is meant to replace the FilterManager found in Panda3D's Direct library.

## Example
The code below was added to the "Roaming Ralph" demo to do HDR rendering.
The full sample can be found in `samples/roaming-ralph`.
```python
        self.render.set_attrib(LightRampAttrib.make_identity())
        fb_props = FrameBufferProperties()
        fb_props.set_float_color(True)
        fb_props.set_rgba_bits(16, 16, 16, 0)
        fb_props.set_depth_bits(32)

        scene_pass = RenderPass(
            'scene',
            camera=base.camera,
            scene=base.render,
            frame_buffer_properties=fb_props,
            clear_color=LColor(0.53, 0.80, 0.92, 1),
        )

        filter_pass = RenderPass(
            'filter',
            shader=Shader.load(Shader.SL_GLSL, 'shaders/fsq.vert', 'shaders/fsq.frag')
        )
        filter_pass._root.set_shader_input('render', scene_pass.output)

        card = filter_pass.buffer.getTextureCard()
        card.setTexture(filter_pass.output)
        card.reparentTo(render2d)
```
