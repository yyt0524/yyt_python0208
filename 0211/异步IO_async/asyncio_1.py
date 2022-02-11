# -*- coding: UTF-8 -*-
import asyncio


async def a():
    print('Suspending a')
    await asyncio.sleep(0)
    print('Resuming a')


async def b():
    print('In b')


async def main():
    await asyncio.gather(a(), b())


if __name__ == '__main__':
    asyncio.run(main())


'''

> **重点**：**异步I/O与多进程的比较**。
>
>   当程序不需要真正的并发性或并行性，而是更多的依赖于异步处理和回调时，
    `asyncio`就是一种很好的选择。如果程序中有大量的等待与休眠时，
    也应该考虑`asyncio`，它很适合编写没有实时数据处理需求的Web应用服务器。

    Python还有很多用于处理并行任务的三方库，例如：`joblib`、`PyMP`等。
    实际开发中，要提升系统的可扩展性和并发性通常有垂直扩展（增加单个节点的处理能力）
    和水平扩展（将单个节点变成多个节点）两种做法。
    可以通过消息队列来实现应用程序的解耦合，消息队列相当于是多线程同步队列的扩展版本，
    不同机器上的应用程序相当于就是线程，而共享的分布式消息队列就是原来程序中的Queue。
    消息队列（面向消息的中间件）的最流行和最标准化的实现是AMQP（高级消息队列协议），
    AMQP源于金融行业，提供了排队、路由、可靠传输、安全等功能，
    最著名的实现包括：Apache的ActiveMQ、RabbitMQ等。

    要实现任务的异步化，可以使用名为`Celery`的三方库。
    `Celery`是Python编写的分布式任务队列，
    它使用分布式消息进行工作，可以基于RabbitMQ或Redis来作为后端的消息代理

'''