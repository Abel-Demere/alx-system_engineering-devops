# Increase the hard file limit for the 'holberton' user
exec { 'limit-for-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

# Increase the soft file limit for the 'holberton' user
exec { 'soft-limit-for-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
