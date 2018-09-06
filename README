# grpc的python及go的学习示例代码

## 运行python grpc
```
make python
make go
python3 server.py
```

## 运行go grpc示例
```
make go
go run main.go
```

## 说明：
grpc的gateway api作用是使用go转发http请求到rpc服务上
所以，我在网关里写了一个针对grpc服务健康检查

### 关于服务发现、负载均衡、重试机制等
grpc是比较底层的服务构建，均不支持这些功能，都需要自己写
consul自带api，可方便进行服务注册及健康检查等
负载均衡可以通过services列表进行随机选择

如果需要更多功能集成，可移步[go-micro](http://micro.mu/)

