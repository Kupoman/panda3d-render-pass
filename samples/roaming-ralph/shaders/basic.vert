#version 330

in vec4 p3d_Vertex;

uniform mat4 p3d_ModelViewMatrix;
uniform mat4 p3d_ProjectionMatrix;

out vec4 position;

void main()
{
    position = p3d_ModelViewMatrix * p3d_Vertex;
    gl_Position = p3d_ProjectionMatrix * position;
}
