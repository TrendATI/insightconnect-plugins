# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Run Nmap scan"


class Input:
    ARGUMENTS = "arguments"
    HOSTS = "hosts"
    PORTS = "ports"
    SUDO = "sudo"
    

class Output:
    RESULT = "result"
    

class ScanInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "arguments": {
      "type": "string",
      "title": "Arguments",
      "description": "Arguments to supply to the Nmap command",
      "order": 3
    },
    "hosts": {
      "type": "string",
      "title": "Hosts",
      "description": "Host(s) to scan in Nmap-allowed formats",
      "order": 1
    },
    "ports": {
      "type": "string",
      "title": "Ports",
      "description": "Port(s) to scan in Nmap-allowed formats",
      "order": 2
    },
    "sudo": {
      "type": "boolean",
      "title": "Sudo",
      "description": "Whether or not to use superuser privileges for scan",
      "default": false,
      "order": 4
    }
  },
  "required": [
    "hosts",
    "sudo"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ScanOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result": {
      "type": "array",
      "title": "Output Results",
      "description": "Scan results",
      "items": {
        "$ref": "#/definitions/host"
      },
      "order": 1
    }
  },
  "definitions": {
    "addresses": {
      "type": "object",
      "title": "addresses",
      "properties": {
        "ipv4": {
          "type": "string",
          "title": "IPv4",
          "description": "IPv4 Address",
          "order": 1
        },
        "ipv6": {
          "type": "string",
          "title": "IPv6",
          "description": "IPv6 Address",
          "order": 2
        }
      }
    },
    "host": {
      "type": "object",
      "title": "host",
      "properties": {
        "addresses": {
          "$ref": "#/definitions/addresses",
          "title": "Addresses",
          "description": "Addresses",
          "order": 1
        },
        "hostnames": {
          "type": "array",
          "title": "Hostnames",
          "description": "Hostnames",
          "items": {
            "$ref": "#/definitions/hostname"
          },
          "order": 2
        },
        "osmatch": {
          "type": "array",
          "title": "OS Matches",
          "description": "OS matches",
          "items": {
            "$ref": "#/definitions/osmatch"
          },
          "order": 3
        },
        "status": {
          "$ref": "#/definitions/status",
          "title": "Status",
          "description": "Status of the host",
          "order": 4
        },
        "tcp": {
          "type": "array",
          "title": "TCP",
          "description": "TCP ports",
          "items": {
            "$ref": "#/definitions/tcp"
          },
          "order": 5
        },
        "udp": {
          "type": "array",
          "title": "UDP",
          "description": "UDP ports",
          "items": {
            "$ref": "#/definitions/udp"
          },
          "order": 6
        },
        "vendor": {
          "type": "object",
          "title": "Vendor",
          "description": "Vendor",
          "order": 7
        }
      },
      "definitions": {
        "addresses": {
          "type": "object",
          "title": "addresses",
          "properties": {
            "ipv4": {
              "type": "string",
              "title": "IPv4",
              "description": "IPv4 Address",
              "order": 1
            },
            "ipv6": {
              "type": "string",
              "title": "IPv6",
              "description": "IPv6 Address",
              "order": 2
            }
          }
        },
        "hostname": {
          "type": "object",
          "title": "hostname",
          "properties": {
            "name": {
              "type": "string",
              "title": "Hostname",
              "description": "Hostname",
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type, eg. PTR",
              "order": 2
            }
          }
        },
        "osclass": {
          "type": "object",
          "title": "osclass",
          "properties": {
            "accuracy": {
              "type": "string",
              "title": "Accuracy",
              "description": "Accuracy of the match",
              "order": 1
            },
            "cpe": {
              "type": "array",
              "title": "CPEs",
              "description": "Common Platform Enumeration addresses",
              "items": {
                "type": "string"
              },
              "order": 2
            },
            "osfamily": {
              "type": "string",
              "title": "OS Family, eg. embedded",
              "description": "OS family",
              "order": 3
            },
            "osgen": {
              "type": "string",
              "title": "OS Generation",
              "description": "OS Generation, eg. 10.7.x (for MacOS)",
              "order": 4
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type of OS",
              "order": 5
            },
            "vendor": {
              "type": "string",
              "title": "Vendor",
              "description": "Vendor",
              "order": 6
            }
          }
        },
        "osmatch": {
          "type": "object",
          "title": "osmatch",
          "properties": {
            "accuracy": {
              "type": "string",
              "title": "Accuracy",
              "description": "Accuracy of the match",
              "order": 1
            },
            "line": {
              "type": "string",
              "title": "Line",
              "description": "Line",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 3
            },
            "osclass": {
              "type": "array",
              "title": "OS Class",
              "description": "OS class",
              "items": {
                "$ref": "#/definitions/osclass"
              },
              "order": 4
            }
          },
          "definitions": {
            "osclass": {
              "type": "object",
              "title": "osclass",
              "properties": {
                "accuracy": {
                  "type": "string",
                  "title": "Accuracy",
                  "description": "Accuracy of the match",
                  "order": 1
                },
                "cpe": {
                  "type": "array",
                  "title": "CPEs",
                  "description": "Common Platform Enumeration addresses",
                  "items": {
                    "type": "string"
                  },
                  "order": 2
                },
                "osfamily": {
                  "type": "string",
                  "title": "OS Family, eg. embedded",
                  "description": "OS family",
                  "order": 3
                },
                "osgen": {
                  "type": "string",
                  "title": "OS Generation",
                  "description": "OS Generation, eg. 10.7.x (for MacOS)",
                  "order": 4
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "description": "Type of OS",
                  "order": 5
                },
                "vendor": {
                  "type": "string",
                  "title": "Vendor",
                  "description": "Vendor",
                  "order": 6
                }
              }
            }
          }
        },
        "status": {
          "type": "object",
          "title": "status",
          "properties": {
            "reason": {
              "type": "string",
              "title": "Reason",
              "description": "Reason, eg. syn-ack",
              "order": 1
            },
            "state": {
              "type": "string",
              "title": "State",
              "description": "State eg. up",
              "order": 2
            }
          }
        },
        "tcp": {
          "type": "object",
          "title": "tcp",
          "properties": {
            "conf": {
              "type": "string",
              "title": "Configuration",
              "description": "Conf",
              "order": 1
            },
            "cpe": {
              "type": "string",
              "title": "CPE",
              "description": "Common Platform Enumeration address",
              "order": 2
            },
            "extrainfo": {
              "type": "string",
              "title": "Extra Info",
              "description": "Extra info",
              "order": 3
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Port name",
              "order": 4
            },
            "port": {
              "type": "integer",
              "title": "Port",
              "description": "Port number",
              "order": 5
            },
            "product": {
              "type": "string",
              "title": "Product",
              "description": "Product",
              "order": 6
            },
            "reason": {
              "type": "string",
              "title": "Reason",
              "description": "Reason, eg. syn-ack",
              "order": 7
            },
            "state": {
              "type": "string",
              "title": "State",
              "description": "State of port, eg. open",
              "order": 8
            },
            "version": {
              "type": "string",
              "title": "Version",
              "description": "Version",
              "order": 9
            }
          }
        },
        "udp": {
          "type": "object",
          "title": "udp",
          "properties": {
            "conf": {
              "type": "string",
              "title": "Configuration",
              "description": "Conf",
              "order": 1
            },
            "cpe": {
              "type": "string",
              "title": "CPE",
              "description": "Common Platform Enumeration address",
              "order": 2
            },
            "extrainfo": {
              "type": "string",
              "title": "Extra Info",
              "description": "Extra info",
              "order": 3
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Port name",
              "order": 4
            },
            "port": {
              "type": "integer",
              "title": "Port",
              "description": "Port number",
              "order": 5
            },
            "product": {
              "type": "string",
              "title": "Product",
              "description": "Product",
              "order": 6
            },
            "reason": {
              "type": "string",
              "title": "Reason",
              "description": "Reason, eg. syn-ack",
              "order": 7
            },
            "state": {
              "type": "string",
              "title": "State",
              "description": "State of port, eg. open",
              "order": 8
            },
            "version": {
              "type": "string",
              "title": "Version",
              "description": "Version",
              "order": 9
            }
          }
        }
      }
    },
    "hostname": {
      "type": "object",
      "title": "hostname",
      "properties": {
        "name": {
          "type": "string",
          "title": "Hostname",
          "description": "Hostname",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type, eg. PTR",
          "order": 2
        }
      }
    },
    "osclass": {
      "type": "object",
      "title": "osclass",
      "properties": {
        "accuracy": {
          "type": "string",
          "title": "Accuracy",
          "description": "Accuracy of the match",
          "order": 1
        },
        "cpe": {
          "type": "array",
          "title": "CPEs",
          "description": "Common Platform Enumeration addresses",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "osfamily": {
          "type": "string",
          "title": "OS Family, eg. embedded",
          "description": "OS family",
          "order": 3
        },
        "osgen": {
          "type": "string",
          "title": "OS Generation",
          "description": "OS Generation, eg. 10.7.x (for MacOS)",
          "order": 4
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of OS",
          "order": 5
        },
        "vendor": {
          "type": "string",
          "title": "Vendor",
          "description": "Vendor",
          "order": 6
        }
      }
    },
    "osmatch": {
      "type": "object",
      "title": "osmatch",
      "properties": {
        "accuracy": {
          "type": "string",
          "title": "Accuracy",
          "description": "Accuracy of the match",
          "order": 1
        },
        "line": {
          "type": "string",
          "title": "Line",
          "description": "Line",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 3
        },
        "osclass": {
          "type": "array",
          "title": "OS Class",
          "description": "OS class",
          "items": {
            "$ref": "#/definitions/osclass"
          },
          "order": 4
        }
      },
      "definitions": {
        "osclass": {
          "type": "object",
          "title": "osclass",
          "properties": {
            "accuracy": {
              "type": "string",
              "title": "Accuracy",
              "description": "Accuracy of the match",
              "order": 1
            },
            "cpe": {
              "type": "array",
              "title": "CPEs",
              "description": "Common Platform Enumeration addresses",
              "items": {
                "type": "string"
              },
              "order": 2
            },
            "osfamily": {
              "type": "string",
              "title": "OS Family, eg. embedded",
              "description": "OS family",
              "order": 3
            },
            "osgen": {
              "type": "string",
              "title": "OS Generation",
              "description": "OS Generation, eg. 10.7.x (for MacOS)",
              "order": 4
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type of OS",
              "order": 5
            },
            "vendor": {
              "type": "string",
              "title": "Vendor",
              "description": "Vendor",
              "order": 6
            }
          }
        }
      }
    },
    "status": {
      "type": "object",
      "title": "status",
      "properties": {
        "reason": {
          "type": "string",
          "title": "Reason",
          "description": "Reason, eg. syn-ack",
          "order": 1
        },
        "state": {
          "type": "string",
          "title": "State",
          "description": "State eg. up",
          "order": 2
        }
      }
    },
    "tcp": {
      "type": "object",
      "title": "tcp",
      "properties": {
        "conf": {
          "type": "string",
          "title": "Configuration",
          "description": "Conf",
          "order": 1
        },
        "cpe": {
          "type": "string",
          "title": "CPE",
          "description": "Common Platform Enumeration address",
          "order": 2
        },
        "extrainfo": {
          "type": "string",
          "title": "Extra Info",
          "description": "Extra info",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Port name",
          "order": 4
        },
        "port": {
          "type": "integer",
          "title": "Port",
          "description": "Port number",
          "order": 5
        },
        "product": {
          "type": "string",
          "title": "Product",
          "description": "Product",
          "order": 6
        },
        "reason": {
          "type": "string",
          "title": "Reason",
          "description": "Reason, eg. syn-ack",
          "order": 7
        },
        "state": {
          "type": "string",
          "title": "State",
          "description": "State of port, eg. open",
          "order": 8
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "Version",
          "order": 9
        }
      }
    },
    "udp": {
      "type": "object",
      "title": "udp",
      "properties": {
        "conf": {
          "type": "string",
          "title": "Configuration",
          "description": "Conf",
          "order": 1
        },
        "cpe": {
          "type": "string",
          "title": "CPE",
          "description": "Common Platform Enumeration address",
          "order": 2
        },
        "extrainfo": {
          "type": "string",
          "title": "Extra Info",
          "description": "Extra info",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Port name",
          "order": 4
        },
        "port": {
          "type": "integer",
          "title": "Port",
          "description": "Port number",
          "order": 5
        },
        "product": {
          "type": "string",
          "title": "Product",
          "description": "Product",
          "order": 6
        },
        "reason": {
          "type": "string",
          "title": "Reason",
          "description": "Reason, eg. syn-ack",
          "order": 7
        },
        "state": {
          "type": "string",
          "title": "State",
          "description": "State of port, eg. open",
          "order": 8
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "Version",
          "order": 9
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
