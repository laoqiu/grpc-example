GATEWAY_FLAGS := -I. -I$(GOPATH)/src -I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis

GRPC_FLAGS := --python_out=. --grpc_python_out=.

python:
	python3 -m grpc_tools.protoc $(GRPC_FLAGS) $(GATEWAY_FLAGS) proto/*/*.proto

go:
	for f in proto/*/*.proto; do \
		protoc $(GATEWAY_FLAGS) \
			--go_out=plugins=grpc:. \
			--grpc-gateway_out=logtostderr=true:. \
			$$f; \
		echo compiled: $$f; \
	done

deps:
	go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway
	go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger
	go get -u github.com/golang/protobuf/protoc-gen-go