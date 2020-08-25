import pyglet
import ratcave as rc
import pywavefront

# Create Window
window = pyglet.window.Window()

def update(dt):
    pass
pyglet.clock.schedule(update)

# Insert filename into WavefrontReader.
obj_filename = rc.resources.obj_primitives
obj_reader = pywavefront.Wavefront('T-shirt model.obj')
#rc.WavefrontReader('T-shirt model.obj')

#print(obj_reader.bodies.keys())
print(obj_reader.meshes)

# Create Mesh
mesh = obj_reader.file_name("Box001")
#mesh = obj_reader.get_mesh("Box001")
mesh.position.xyz = 0, 0, -2

# Create Scene
scene = rc.Scene(meshes=[mesh])

@window.event
def on_draw():
    with rc.default_shader:
        scene.draw()

pyglet.app.run()