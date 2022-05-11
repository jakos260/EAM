clear all
close all
clc

% dt = readtable('S1_0001.txt');
dt = csvread("s1.csv")

x = dt(:,1);
accX = dt(:,3);
accY = dt(:,4);
accZ = dt(:,5);

figure(1)
hold on
plot(x,accX)
plot(x,accY)
plot(x,accZ)
grid on
legend('accX','accY','accZ')
hold off

Q0 = dt(:,12);
Q1 = dt(:,13);
Q2 = dt(:,14);
Q3 = dt(:,15);

figure(2)
hold on
plot(x,Q0)
plot(x,Q1)
plot(x,Q2)
plot(x,Q3)
grid on
legend('Q0','Q1', 'Q2', 'Q3')
hold off

q = quaternion(Q0, Q1, Q2, Q3)

dr.drawEulerRotation(q)
