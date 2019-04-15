#version 330

in vec4 position;
out vec4 out_data;

void main()
{
    out_data.rgba = position * vec4(0.1);
}
