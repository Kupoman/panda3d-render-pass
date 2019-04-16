#version 330

uniform sampler2D render;

in vec2 texcoord;
out vec4 out_data;

void main()
{
    vec3 color = texture(render, texcoord).rgb;
    color = color / (color + vec3(1.0));
    color = pow(color, vec3(1.0/2.2));
    out_data.rgb = color;
    out_data.a = 1.0;
}
