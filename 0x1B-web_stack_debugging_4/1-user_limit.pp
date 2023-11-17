# Increase the hard file limit for the 'holberton' user
exec { 'replace-the-limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin'],
}

# Increase the soft file limit for the 'holberton' user
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
