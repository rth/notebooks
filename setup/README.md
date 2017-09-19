
```

wget -O - https://raw.githubusercontent.com/rth/notebooks/master/setup/setup_ec2.sh | bash
```


## Docker cheatsheet

* Remove all non active containers,
  ```
  docker ps -a | awk '{print $1}' | xargs docker rm
  ```
* Remove all dangling images,
  ```
  docker rmi $(docker images -f dangling=true -q)
  ```
