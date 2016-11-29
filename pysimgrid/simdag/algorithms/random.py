# This file is part of pysimgrid, a Python interface to the SimGrid library.
#
# Copyright 2015-2016 Alexey Nazarenko and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# along with this library.  If not, see <http://www.gnu.org/licenses/>.
#

import random
from .. import scheduler
from .. import taskflow

class RandomScheduler(scheduler.StaticScheduler):
  """
  Random static scheduler implementation.

  The important part there is static - all tasks are scheduled simultaneously.
  Resulting schedule is significantly worse than dynamic random schedule. In static
  case task may wait for their parents execution for a quite some time (blocking some other tasks),
  while dynamic approach guarantees that parents are already done.

  The point of this scheduler is to be an 'worst' static scheduler as a reference point
  for sensible algorithms.
  """
  def get_schedule(self, simulation):
    schedule = {host: [] for host in simulation.hosts}
    ids_tasks = {task.name: task for task in simulation.tasks}
    flow = taskflow.Taskflow()
    flow.from_simulation(simulation)
    for task in flow.topological_order():
      schedule[random.choice(simulation.hosts)].append(ids_tasks[task])
    return schedule
