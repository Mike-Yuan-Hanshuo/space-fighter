# GlowScript 3.2 VPython

# Create the scene
scene = canvas(title="Destroy Earth Simulation",
               width=800, height=600,
               center=vec(0, 0, 0),
               background=color.black)

# Adjust the camera position and zoom
scene.camera.pos = vec(0, 2, 12)
scene.camera.axis = vec(0, -1, -12)

# Earth creation
earth = sphere(pos=vec(0, 0, 0), radius=2, texture=textures.earth)

# Title and instructions
instructions = label(pos=vec(0, 4.5, 0), text="Choose a way to destroy Earth!", 
                     color=color.white, height=16, box=False, align='center')

# Store initial state
initial_state = {
    "earth_pos": vec(0, 0, 0),
    "earth_radius": 2,
    "earth_texture": textures.earth
}

# Define the Earth destruction logic
def destroy_earth(method):
    if method == "asteroid":
        instructions.text = "Asteroid is heading toward Earth..."
        asteroid = sphere(pos=vec(-5, 0, 0), radius=0.5, color=color.red, make_trail=True)
        velocity = vec(10, 0, 0)
        while mag(asteroid.pos - earth.pos) > earth.radius:
            rate(100)
            asteroid.pos += velocity * 0.02
        asteroid.visible = False
        earth.visible = False
        explosion_effect(earth.pos)
        instructions.text = "Earth was destroyed by an asteroid!"
    
    elif method == "explosion":
        instructions.text = "Earth is exploding..."
        earth.visible = False
        explosion_effect(earth.pos)
        instructions.text = "Earth was obliterated in an explosion!"

    elif method == "black_hole":
        instructions.text = "Black hole is swallowing Earth..."
        black_hole = sphere(pos=vec(3, 0, 0), radius=1, color=color.black, emissive=True)
        while mag(earth.pos - black_hole.pos) > 0.1:
            rate(100)
            earth.pos += norm(black_hole.pos - earth.pos) * 0.05
        earth.visible = False
        instructions.text = "Earth was swallowed by a black hole!"
    
    elif method == "laser_beam":
        instructions.text = "Laser beam is destroying Earth..."
        laser = cylinder(pos=vec(0, 5, 0), axis=vec(0, -6, 0), radius=0.1, color=color.red)
        for _ in range(100):
            rate(50)
            laser.radius += 0.01
        earth.visible = False
        laser.visible = False
        instructions.text = "Earth was annihilated by a laser beam!"
    
    elif method == "flood":
        instructions.text = "Flood is submerging Earth..."
        water = sphere(pos=vec(0, 0, 0), radius=earth.radius, color=color.blue, opacity=0.5)
        while water.radius < 3:
            rate(50)
            water.radius += 0.05
        earth.visible = False
        instructions.text = "Earth was submerged in a massive flood!"

    elif method == "supernova":
        instructions.text = "Supernova explosion is destroying Earth..."
        star = sphere(pos=vec(-5, 0, 0), radius=0.5, color=color.yellow, emissive=True)
        while star.radius < 5:
            rate(50)
            star.radius += 0.1
        earth.visible = False
        star.visible = False
        explosion_effect(earth.pos)
        instructions.text = "Earth was obliterated by a supernova!"

# Explosion effect
def explosion_effect(position):
    fragments = []
    for _ in range(30):
        fragment = sphere(pos=position, radius=0.1, color=color.orange, make_trail=True)
        fragment.velocity = vec(random()-0.5, random()-0.5, random()-0.5) * 5
        fragments.append(fragment)
    for _ in range(100):
        rate(50)
        for fragment in fragments:
            fragment.pos += fragment.velocity * 0.1

# Reset function
def reset_simulation():
    global earth
    earth.visible = False  # Hide the destroyed Earth (if any)
    earth = sphere(pos=initial_state["earth_pos"],
                   radius=initial_state["earth_radius"],
                   texture=initial_state["earth_texture"])
    instructions.text = "Choose a way to destroy Earth!"

# Button callback functions
def asteroid_impact(): destroy_earth("asteroid")
def explosion(): destroy_earth("explosion")
def black_hole(): destroy_earth("black_hole")
def laser_beam(): destroy_earth("laser_beam")
def flood(): destroy_earth("flood")
def supernova(): destroy_earth("supernova")

# Create the buttons
x_offset = -180  # Adjust horizontal spacing
y_offset = 30    # Adjust vertical spacing
button_width = 120  # Adjust button width

button(text="Asteroid Impact", bind=asteroid_impact)
button(text="Explosion", bind=explosion)
button(text="Black Hole", bind=black_hole)
button(text="Laser Beam", bind=laser_beam)
button(text="Flood", bind=flood)
button(text="Supernova", bind=supernova)
button(text="Reset", bind=reset_simulation)

