train = load("spam_train.data")
train(1,:)
train_x = train(1:end)
train_x = train(1:57)
train_x = train(:,:end-1)
train_x = train(:,:)
train_x = train(:,:57)
train_x = train(:,1:57)
train_x(1,:)
train(1,:)
train_y = train(:,57:)
train_y = train(:,57:end)
train_t
train_y
train_y = train(:,end:end)
H = eye(57 + 1 + 3000)
H(58:end,58:end)=0
C = 1
f = C ones(57+1+3000,1)
f = C * ones(57+1+3000,1)
f
f(1:58)=0
train_y
y = zeros(3000,1)
y(labels == 2) = =-1
y(labels == 2) = -1
y(train_y == 2) = -1
y(train_y == 1) = 1
y(train_y == 0) = -1
y
A =   repmat(y,1,58) .* [x ones(3000,1)];
A =   repmat(y,1,58) .* [train_x ones(3000,1)];
A = -1*[A eye(3000)];
b = -1 * ones(3000, 1);
opts = optimset('Algorithm','active-set','Display','on');
w = quadprog(H, f, A, b, [], [], [], [], [], opts)