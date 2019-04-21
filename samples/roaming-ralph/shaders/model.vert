#version 330

in vec4 p3d_Vertex;
in vec3 p3d_Normal;
in vec2 p3d_MultiTexCoord0;

uniform mat4 p3d_ModelViewMatrix;
uniform mat4 p3d_ProjectionMatrix;
uniform mat3 p3d_NormalMatrix;

out vec4 position;
out vec3 normal;
out vec2 texcoord;

void main()
{
    position = p3d_ModelViewMatrix * p3d_Vertex;
    normal = p3d_NormalMatrix * p3d_Normal;
    texcoord = p3d_MultiTexCoord0;
    gl_Position = p3d_ProjectionMatrix * position;
}
