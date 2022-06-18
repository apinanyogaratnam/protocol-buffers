proto:
	arch -x86_64 python -m grpc_tools.protoc -I./protos protos/square_root.proto --python_out=. --grpc_python_out=.
