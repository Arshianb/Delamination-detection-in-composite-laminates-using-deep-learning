clc
clear all
close all

filename = "C:\Users\795593\OneDrive\Desktop\Delamination-detection-in-composite-laminates-using-deep-learning\MeshStudy-output.csv";
freqs = readmatrix(filename);
meshSize = freqs(:, 1);


meshes = [
    0.04 
    0.0341299129913 
    0.0204785478548 
    0.0146259625963 
    0.0113776377638 
    0.00930893089309 
    0.00787378737874 
    0.00682368236824 
    0.00602210221022 
    0.00538853885389 
]*1000;

index = 1;
figure('Renderer', 'painters', 'Position', [10 10 1000 700])
for i = 2:21
    if i < 20
        subplot(3,2,index)
    else
        subplot(2,1,index)
    end
    
    index = index + 1;
    freq = freqs(:, i);
    plot(meshes, freq, 'oblack', 'MarkerSize', 8, 'MarkerFaceColor', 'red');
%     text(meshes(3), freq(3)+freq(3)*0.03,sprintf("x = %.4f\ny = %.2f\n", meshes(3), freq(3)))
%     text(meshes(4)-meshes(4)*0.15, freq(4)+freq(4)*0.03,sprintf("x = %.4f\ny = %.2f\n", meshes(4), freq(4)))
%     text(meshes(3), freq(3),sprintf("x = %f\ny = %f\n", meshes(3), freq(3)))
    p = polyfit(meshes, freq, 5);
    x = 0.005*1000:0.0001:0.04*1000;
    y = polyval(p, x);  
    hold on
    plot(x, y, 'black', 'linewidth', 4)
    xlabel("Mesh Size (mm)")
    ylabel("natural Frequency")
    title(sprintf("Modal frequency Num %i", i))
    grid minor
    if index == 7
        figure('Renderer', 'painters', 'Position', [10 10 1000 700])
        index = 1;
    end
end