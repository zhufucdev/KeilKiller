# Keil Killer

It's basically a re-encoding tool made in Python.

As we all know, Keil is a shitty ancient software that can 
work without Unicode support, in Chinese countries specifically,
using GB2312, which is a disaster for modern IDEs to adopt.

Hope no one would be using this.

## Usage

Pull all dependencies by
```shell
pip install -r requirements.txt
```

Start converting
```shell
python main.py extract <Keil Project Root> <Output Dir> --encoding=<You determinate>
```

The program will iterate through all files under 
`<Keil Project Root>/Libraries`

## License
```
Copyright 2022 zhufucdev

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```