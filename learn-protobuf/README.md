# learn-protobuf

The examples here follow most of what is included within the python protobuf tutorial provided by Google (https://developers.google.com/protocol-buffers/docs/pythontutorial).  However here proto3 sytax is used within the .proto files and an alternative compiler plugin, python-betterproto, is used which provides for more pythonic usage, including taking advantage of dataclasses.  (https://github.com/danielgtaylor/python-betterproto)

## Installation
Recommended Python Version: 3.8 +

Install the requirements from the requirements.txt file.

You must also install the protoc binary compiler which can be found here: (https://developers.google.com/protocol-buffers/docs/downloads)

## Follow Along
1. To use protobuf you must define your protocol format.  This has already been done in the `protocols/addressbook.proto`.  The protocol format will then be converted to a language of choice to consume, which in this case will be python.

    > **_NOTE:_**  You might notice that `required` and `optional` has been removed from protocol format due to the fact that it is seen as an anti-pattern now.  It seems this debate has been long lived and there are camps on boths sides of the issue.  There are lots of resouces to read about the debate but I found this link helpful (https://stackoverflow.com/questions/31801257/why-required-and-optional-is-removed-in-protocol-buffers-3)

2. To convert the protocol format to a protocol buffer use the protocol compiler, `protoc`, which is provided by Google.  In the root of `learn-protobuf` run the following: 

    ```bash
    protoc -I ./protocols --python_out=./protobuf3 ./protocols/addressbook.proto
    ```

    > **_NOTE:_**  If you are following along and want to see this file generated remove the existing file `addressbook_pb2.py` from the protobuf3 directory

    After running the protoc command you will see the generated python classes which will allow you to read and write the messages defined in the protocol format.  It should be in the `protobuf3` directory and named `addressbook_pb2.py`.  You will also need to make your module importable so add in a `__init__.py` file in the `protobug3` directory.

3. To write messages with the API that was generated in the previous step you simply import the protocol API module (created in the previous step), create the message classes, and populate the data.  When you are done with writing you data you then serialize your data with the method `SerializeToString()`  You can see an example of this in the file `proto3_write.py`.  This file is a script that you can execute which takes one filename argurment, which is the file that will be created. 

    ```bash
    python proto3_write.py serialized/proto3_addressbook
    ```

    After writing your message and serializing your data you should have a file with you your serialized data `serialized/proto3_addressbook`

4. To read serialized messages you will then consume the file that was created in the previous step, and parse the serialized data with the protocol API module (created in step 2).  You can consume the serialized data with the method ParseFromString().  You can see an example of this in the file `proto3_read.py`  This file is a script that you can execute whch takes one filename argument, which is the file that will be read (this file was created in step 3).

    ```bash
    python proto3_read.py serialized/proto3_addressbook
    ```

These steps highlight the basic definition, writing of data with the protobuf API, and reading data with protobuf API.  In this case you could retrieve data from a database, package it with the protobuf API, and send it off to the consumer, who can unpackage it and store data in whatever way they want to consume it.  Because it was all written with the protobuf API both the writer and the consumer know how the data will be structured.  The producer cannot add fields to the data if it does not exist within the defined protocol file and the consume cannot consume data likewise.  Protobuf also writes all the data in bytes which reduces the size of the data that will be produced and sent between the producer and consumer.

If you are paying attention to the generated protocol API file you might notice that it does not produce easily readable code.  It also does not take advantage of some of the features such as Dataclasses and typing.  If you are using an IDE with intellisense you also do not get any of the code completion that you would normally see.  There is a solution for this in the `python-betterproto` library which I was turned onto. (https://github.com/danielgtaylor/python-betterproto).

## python-beterproto

1. To convert the protocol format to a protocol buffer use the protocol compiler, `protoc`, which is provided by Google with the `python_betterproto_out` add-on compiler.  In the root of `learn-protobuf` run the following: 

    ```bash
    protoc -I ./protocols --python_betterproto_out=./better ./protocols/addressbook.proto
    ```

    > **_NOTE:_**  If you are following along and want to see this file generated remove the existing directory `better` from the learn-protobuf root

    After running the protoc command you will see the generated python dataclasses which will allow you to read and write the messages defined in the protocol format.  It should be in the `better` directory and named `tutorial.py`.  You will notice the protocol API generated with betterproto is much more pythonic and easier to read then the protocol API that was generated with the Google python compiler.

2. To write messages with the API that was generated in the previous step you simply import the protocol API module (created in the previous step), create the message classes, and populate the data.  When you are done with writing you data you then serialize your data with the bytes built-in function.  You can see an example of this in the file `better_write.py`.  This file is a script that you can execute which takes one filename argurment, which is the file that will be created. 

    ```bash
    python better_write.py serialized/better_addressbook
    ```

    After writing your message and serializing your data you should have a file with you your serialized data `serialized/better_addressbook`

3. To read serialized messages you will then consume the file that was created in the previous step, and parse the serialized data with the protocol API module (created in step 1).  You can consume the serialized data with the method parse().  You can see an example of this in the file `better_read.py`  This file is a script that you can execute whch takes one filename argument, which is the file that will be read (this file was created in step 2).

    ```bash
    python better_read.py serialized/better_addressbook
    ```

## Typed serialized data through the protocol API.
If you serialized your data with both the Google default python compiler and the betterproto compiler you will have 2 unique serialized files, `serialized/proto3_addressbook` and `serialized/better_addressbook`.  To prove that the serialized data can be read between the two you can run the respective read file against the serialized data that was built with the others API.


## Pros and cons of protobuf over standard JSON
> **_NOTE:_**  Not comprehensive but what I learned while reading about and experimenting with protobuf on my own.

**Pros**
- Structured data that is predefined
- Type validated at time of serialization
- Data is transferred in binary, reducing the data size from standard JSON
- Language netural via compilers that are written for other languages

**Cons**
- Binary data is not human readable on its own
- Data must be structured
- Uses third party libraries, opening up possiblities of unknown bugs
