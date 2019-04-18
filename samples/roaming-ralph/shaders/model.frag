#version 330

in vec4 position;
in vec3 normal;
in vec2 texcoord;

uniform sampler2D p3d_Texture0;

layout(location=0) out vec4 out_data;
layout(location=1) out vec4 out_data1;

void main()
{
    vec3 color = texture(p3d_Texture0, texcoord).rgb;
    color = color * vec3(2.2);
    out_data.rgba = vec4(color, 1.0);
    out_data1.rgba = vec4(normal, 1.0);
}
