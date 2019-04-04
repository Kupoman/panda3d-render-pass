import pytest


import panda3d.core as p3d

from panda3d_render_pass import RenderPass

def create_window(engine, pipe):
    fbprops = p3d.FrameBufferProperties()
    fbprops.set_rgba_bits(8, 8, 8, 0)
    fbprops.set_depth_bits(24)
    winprops = p3d.WindowProperties.size(1, 1)
    flags = p3d.GraphicsPipe.BF_refuse_window
    return engine.make_output(
        pipe,
        'window',
        0,
        fbprops,
        winprops,
        flags
    )

@pytest.fixture
def default_args():
    pipe = p3d.GraphicsPipeSelection.get_global_ptr().make_default_pipe()
    engine = p3d.GraphicsEngine(pipe)
    window = create_window(engine, pipe)
    return {
        'pipe': pipe,
        'engine': engine,
        'window': window,
        'camera': p3d.NodePath(p3d.Camera('camera', p3d.PerspectiveLens()))
    }


def test_create_output(default_args):
    engine = default_args['engine']
    initial_win_count = len(engine.get_windows())
    rpass = RenderPass('test', **default_args)
    engine.render_frame()
    assert len(engine.get_windows()) == initial_win_count + 1
    assert type(rpass.buffer == p3d.GraphicsOutput)

    assert rpass.display_region.get_camera() == default_args['camera']
