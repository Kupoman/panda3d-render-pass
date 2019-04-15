#version 330

const vec2 quad_vertices[4] = vec2[4]( vec2( -1.0, -1.0), vec2( 1.0, -1.0), vec2( -1.0, 1.0), vec2( 1.0, 1.0));
const vec2 quad_texcoords[4] = vec2[4]( vec2( 0.0, 0.0), vec2( 1.0, 0.0), vec2( 0.0, 1.0), vec2( 1.0, 1.0));

out vec2 texcoord;

void main()
{
    texcoord = quad_texcoords[gl_VertexID];
    gl_Position = vec4(quad_vertices[gl_VertexID], 0.0, 1.0);
}
