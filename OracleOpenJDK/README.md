Oracle Java OpenJDK on Docker
=====
This repository contains sample Docker configurations to facilitate installation and environment setup for DevOps users. This project includes Dockerfiles for Oracle OpenJDK based on Oracle Linux.

## Building the Oracle Java OpenJDK base image
Navigate to the folder containing the Dockerfile and run docker build, tagging the image with the version number:

e.g. for OpenJDK 15 run
```
$ cd ../OracleOpenJDK/15
$ docker build -t oracle/openjdk:15 .
```

This command is already scripted in build.sh so you can alternatively run:
```
$ bash build.sh
```

## License
The OpenJDK compressed archive used by this Dockerfile is available under the [GNU General Public License, version2, with the Classpath Exception](https://openjdk.java.net/legal/gplv2+ce.html), from the [Oracle OpenJDK website](https://jdk.java.net).
Oracle Linux is licensed under the [Oracle Linux End-User License Agreement](https://oss.oracle.com/ol/EULA).

All scripts and files hosted in this project and GitHub [`docker/OracleOpenJDK`](./) repository, required to build the Docker images are, unless otherwise noted, released under the [UPL 1.0](https://oss.oracle.com/licenses/upl/) license.
