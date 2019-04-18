#version 330

const vec2 quad_vertices[4] = vec2[4]( vec2( -1.0, -1.0), vec2( 1.0, -1.0), vec2( -1.0, 1.0), vec2( 1.0, 1.0));
const vec2 quad_texcoords[4] = vec2[4]( vec2( 0.0, 0.0), vec2( 1.0, 0.0), vec2( 0.0, 1.0), vec2( 1.0, 1.0));

uniform mat4 p3d_ViewMatrix;

out vec2 texcoord;
out vec3 light_dir;

void main()
{
    light_dir = (p3d_ViewMatrix * vec4(-5.0, -5.0, -5.0, 0.0)).xyz;
    texcoord = quad_texcoords[gl_VertexID];
    gl_Position = vec4(quad_vertices[gl_VertexID], 0.0, 1.0);
}
