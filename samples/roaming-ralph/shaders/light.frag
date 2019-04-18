#version 330

uniform sampler2D albedo_texture;
uniform sampler2D normal_texture;

in vec2 texcoord;
in vec3 light_dir;
out vec4 out_data;

void main()
{
    vec3 albedo = texture(albedo_texture, texcoord).rgb;
    vec3 normal = texture(normal_texture, texcoord).rgb;
    float light = max(dot(normal, -normalize(light_dir)), 0.0) + 0.3;
    out_data.rgb = vec3(albedo * light);
    out_data.a = 1.0;
}
